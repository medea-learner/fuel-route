from django.contrib.gis.db import models

class FuelPrice(models.Model):
    truckstop_name = models.CharField(max_length=255)
    address = models.TextField()
    location = models.PointField(geography=True, null=True, blank=True)
    state = models.CharField(max_length=2)
    retail_price = models.FloatField()
