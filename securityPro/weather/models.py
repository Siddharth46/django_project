from django.db import models

# Create your models here.
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)

class City(models.Model):
    name = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=9, decimal_places=3)
    latitude = models.DecimalField(max_digits=9, decimal_places=3)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class Weather(models.Model):
    city = models.OneToOneField(City, on_delete=models.CASCADE)
    min_temp = models.DecimalField(max_digits=5, decimal_places=2)
    max_temp = models.DecimalField(max_digits=5, decimal_places=2)
    feels_like = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    sunrise = models.IntegerField()
    sunset = models.IntegerField()
