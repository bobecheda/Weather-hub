from django.db import models
from django.contrib.auth.models import User

class WeatherSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='weather_searches')
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.IntegerField()
    wind_speed = models.FloatField()
    description = models.CharField(max_length=200)
    icon = models.CharField(max_length=10)

    class Meta:
        ordering = ['-timestamp']
        verbose_name_plural = 'Weather Searches'

    def __str__(self):
        return f'{self.city}, {self.country} - {self.timestamp}'

class FavoriteLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_locations')
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'city', 'country']
        ordering = ['city']

    def __str__(self):
        return f'{self.city}, {self.country}'