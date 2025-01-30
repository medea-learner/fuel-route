import reverse_geocode
from rest_framework import serializers

class RouteRequestSerializer(serializers.Serializer):
    start = serializers.ListField(child=serializers.FloatField(), min_length=2, max_length=2)
    end = serializers.ListField(child=serializers.FloatField(), min_length=2, max_length=2)

    def validate_start(self, value):
        """
        Ensure the start location is within the U.S. boundaries.
        """
        lat, lon = value
        if not self._is_within_us(lat, lon):
            raise serializers.ValidationError("Start location is outside U.S. territory.")
        return value

    def validate_end(self, value):
        """
        Ensure the end location is within the U.S. boundaries.
        """
        lat, lon = value
        if not self._is_within_us(lat, lon):
            raise serializers.ValidationError("End location is outside U.S. territory.")
        return value

    def _is_within_us(self, lat, lon):
        """
        Use reverse geocoding to check if the location is in the U.S.
        Returns True if the location is in the U.S., False otherwise.
        """
        location = reverse_geocode.get((lon, lat))
        if location and location["country"] == "United States":
            return True
        return False
