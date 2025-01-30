import requests
import time
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from django.conf import settings
from geopy.geocoders import OpenCage, Nominatim
from api.models import FuelPrice
from api.utils import load_cleaned_fuel_data

class Command(BaseCommand):
    help = 'Import fuel price data into the FuelPrice model with geolocation'

    def handle(self, *args, **kwargs):
        nominatim_geolocator = Nominatim(user_agent="fuel_price_importer")    
        opencage_geolocator = OpenCage(api_key=settings.OPEN_CAGE_API_KEY)
        locationiq_base_url = f"https://us1.locationiq.com/v1/search.php?key={settings.LOCATIONIQ_API_KEY}"

        cleaned_data = load_cleaned_fuel_data()
        
        for _, row in cleaned_data.iterrows():
            address = f"{row['Address']}, {row['City']}, {row['State']}, USA"
            
            fuel_price, _ = FuelPrice.objects.get_or_create(
                truckstop_name=row['Truckstop Name'],
                address=row['Address'],
                state=row['State'],
                retail_price=row['Retail Price']
            )

            print("Processing address:", address)

            if fuel_price.location:
                continue
            
            # use Nominatim for geocoding
            try:
                location = nominatim_geolocator.geocode(address, timeout=10)
                if location:
                    fuel_price.location = Point(location.longitude, location.latitude)
                    fuel_price.save()
                    time.sleep(1)
                    continue
            except Exception:
                ...

            # Use OpenCage geocoding
            try:
                location = opencage_geolocator.geocode(address, timeout=10)
                if location:
                    fuel_price.location = Point(location.longitude, location.latitude)
                    fuel_price.save()
                    time.sleep(1)
                    continue
            except Exception:
                ...


            # Use LocationIQ for geocoding
            try:
                response = requests.get(f"{locationiq_base_url}&q={address}&format=json")
                if response.status_code == 200:
                    data = response.json()
                    if data:
                        fuel_price.location = Point(data[0]["lon"], data[0]["lat"])
                        fuel_price.save()
                        time.sleep(1)
                        continue
            except Exception:
                ...
            self.stdout.write(self.style.WARNING(f"Could not geocode: {address}"))
            
        self.stdout.write(self.style.SUCCESS('Successfully imported fuel data with geolocation'))
