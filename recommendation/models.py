# recommendation/models.py
from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=100)
    optimal_temperature = models.DecimalField(max_digits=5, decimal_places=2)
    optimal_humidity = models.DecimalField(max_digits=5, decimal_places=2)
    planting_season = models.CharField(max_length=100)
    harvesting_season = models.CharField(max_length=100)
    # Add more fields as needed
# models.py

from django.db import models

class SoilContent(models.Model):
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    ph_level = models.FloatField()

