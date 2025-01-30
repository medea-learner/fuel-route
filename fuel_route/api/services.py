import openrouteservice
import polyline
import pandas as pd
from django.conf import settings
from django.core.cache import cache
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point
from geopy.distance import geodesic
from .utils import directions_response2, generate_cache_key
from .models import FuelPrice


def get_directions(start, end):
    """
    Fetch driving directions between two locations using the OpenRouteService API.

    :param start: Tuple (latitude, longitude) representing the starting location.
    :param end: Tuple (latitude, longitude) representing the destination.
    :return: JSON response containing route details.
    """
    cache_key = generate_cache_key(start, end)
    cached_data = cache.get(cache_key)
    if cached_data:
        return cached_data

    client = openrouteservice.Client(key=settings.ORS_API_KEY)
    directions = client.directions(coordinates=[start, end], profile='driving-car')
    # directions = directions_response2
    '''
    Caching is set to 1 hour (3600 seconds) to reduce API calls and improve response times.
    However, since route data can change due to traffic or road closures, a shorter cache 
    duration (e.g., 10-15 minutes) might be more suitable in dynamic environments. 
    Adjust the timeout based on how frequently route data is expected to change.
    '''
    cache.set(cache_key, directions, timeout=3600)  # Cache for 1 hour
    return directions

def get_route_with_stops(start, end):
    """
    Retrieve a route with fuel stops based on the cheapest fuel prices along the way,  
            **** assuming the car is fully fueled at the beginning. ****

    :param start: Tuple (latitude, longitude) representing the starting location.
    :param end: Tuple (latitude, longitude) representing the destination.
    :return: Tuple containing:
             - decoded_route: List of (latitude, longitude) tuples representing the route.
             - stops_df: Pandas DataFrame with details of the cheapest fuel stops along the route.
    """
    directions = get_directions(start, end)
    if not directions or 'routes' not in directions:
        return None, pd.DataFrame()

    route = directions['routes'][0]
    decoded_route = polyline.decode(route['geometry'])
    
    # Calculate cumulative distances for route points
    cumulative_distances = [0.0]
    for i in range(1, len(decoded_route)):
        cumulative_distances.append(
            cumulative_distances[-1] + 
            geodesic(decoded_route[i-1], decoded_route[i]).miles
        )

    # Split route into 400-mile segments (conservative for 500-mile range)
    segments = []
    current_segment = 0
    while current_segment < cumulative_distances[-1]:
        # Find midpoint of current segment
        end_segment = current_segment + 400
        if end_segment > cumulative_distances[-1]:
            break
        idx = next(i for i, d in enumerate(cumulative_distances) if d >= end_segment)
        midpoint = decoded_route[idx//2]
        segments.append({
            'start_mile': current_segment,
            'end_mile': end_segment,
            'midpoint': Point(midpoint[1], midpoint[0]),  # (lon, lat)
        })
        current_segment = end_segment

    # Find cheapest station near each segment's midpoint
    stops = []
    for segment in segments:
        # Find cheapest station within 50 miles of midpoint
        cheapest = FuelPrice.objects.filter(
            location__dwithin=(segment['midpoint'], D(mi=50))
        ).order_by('retail_price').first()
        
        if cheapest:
            stops.append({
                'mile_position': segment['start_mile'],
                'name': cheapest.truckstop_name,
                'price': cheapest.retail_price,
                'location': [cheapest.location.y, cheapest.location.x]
            })

    return decoded_route, pd.DataFrame(stops)

def calculate_fuel_cost(route_distance, stops):
    """
    Calculate the estimated fuel cost for a given route based on fuel prices at stops.

    :param route_distance: Total route distance in miles.
    :param stops: List of dictionaries containing fuel stop details, including 'retail_price'.
    :return: Estimated fuel cost in dollars.
    """
    if not stops:
        return 0

    # Split route into segments between stops
    segments = []
    prev_stop = 0

    for stop in stops:
        segments.append(min(500, stop['mile_position'] - prev_stop))
        prev_stop = stop['mile_position']
    
    # Add final segment if needed
    final_segment = route_distance - prev_stop
    if final_segment > 0:
        segments.append(final_segment)

    # Calculate cost using cheapest available price for each segment
    total_cost = 0
    price_idx = 0
    for seg_length in segments:
        if price_idx < len(stops):
            price = stops[price_idx]['price']
            price_idx += 1
        else:  # Use last known price if no more stops
            price = stops[-1]['price']
        
        total_cost += (seg_length / 10) * price

    return round(total_cost, 2)


def calculate_route_distance(route):
    """
    Calculate the total distance of a route based on decoded coordinates.

    :param route: List of (latitude, longitude) tuples representing the route.
    :return: Total distance in miles.
    """
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += geodesic(route[i], route[i + 1]).miles
    return total_distance

def generate_google_maps_map_url(route):
    """
    Generate a static map URL for large routes by simplifying and polyline encoding.
    """
    base_url = "https://maps.googleapis.com/maps/api/staticmap?"
    
    # Simplify the route to reduce points
    simplified_route = simplify_route(route, tolerance=0.001, every_n=5)
    
    # Encode the simplified route
    encoded_polyline = encode_polyline(simplified_route)
    
    # Build URL
    path_param = f"path=enc:{encoded_polyline}"
    markers = "&".join([f"markers=color:red%7C{lat},{lon}" for lat, lon in [route[0], route[-1]]])
    return f"{base_url}{path_param}&{markers}&size=600x400&key={settings.GOOGLE_MAPS_API_KEY}"

def generate_ors_map_url(route):
    """
    Generate an OpenRouteService map URL with an encoded polyline.
    Simplifies the route to stay within browser URL limits.
    """
    simplified_route = simplify_route(route, tolerance=0.001, every_n=5)
    encoded_polyline = encode_polyline(simplified_route)
    
    return f"https://openrouteservice.org/maps/?p={encoded_polyline}&mode=drive"

def simplify_route(route, tolerance=None, every_n=None):
    """
    Downsample points using either:
    - Ramer-Douglas-Peucker algorithm (complexity-based)
    - Take every nth point (faster)
    """
    if tolerance:
        # Use simplification library: `pip install simplification`
        from simplification.cutil import simplify_coords
        return simplify_coords(route, tolerance)
    elif every_n:
        return route[::every_n]  # Simple downsampling
    return route

def encode_polyline(points):
    """Encodes a list of (lat, lon) tuples into a polyline string."""
    encoded = []
    prev_lat = 0
    prev_lng = 0
    for lat, lng in points:
        lat_e5 = int(round(lat * 1e5))
        lng_e5 = int(round(lng * 1e5))
        d_lat = lat_e5 - prev_lat
        d_lng = lng_e5 - prev_lng
        encoded.append(_encode_number(d_lat))
        encoded.append(_encode_number(d_lng))
        prev_lat, prev_lng = lat_e5, lng_e5
    return ''.join(encoded)


def _encode_number(number):
    """Encodes a number using the polyline algorithm."""
    number = number << 1
    if number < 0:
        number = ~number
    encoded = []
    while number >= 0x20:
        encoded.append((0x20 | (number & 0x1F)) + 63)
        number >>= 5
    encoded.append(number + 63)
    return ''.join(chr(byte) for byte in encoded)
