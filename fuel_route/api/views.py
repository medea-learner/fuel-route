from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import RouteRequestSerializer
from api.services import (
    get_route_with_stops, calculate_route_distance,
    calculate_fuel_cost, generate_google_maps_map_url
)


class RouteView(APIView):
    def post(self, request):
        serializer = RouteRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
    
        start = serializer.validated_data['start']
        end = serializer.validated_data['end']

        # Get the route and stops
        route, stops_df = get_route_with_stops(start, end)

        if route is None:
            return Response(
                {"error": "Unable to find a route"}, 
                status=400
            )

        # Calculate the total distance of the route (In miles)
        route_distance = calculate_route_distance(route)

        # Prepare stops data
        stop_data = stops_df.to_dict(orient='records')

        # Calculate total fuel cost
        total_fuel_cost = calculate_fuel_cost(route_distance, stop_data)

        # Generate the map URL
        map_url = generate_google_maps_map_url(route)

        # Format the response
        return Response({
            "route": route,  # A list of coordinates (lat, lon)
            "fuel_stops": stop_data,
            "total_fuel_cost": total_fuel_cost,
            "map_url": map_url
        })
