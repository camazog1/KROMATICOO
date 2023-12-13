from django.db import models

# Create your models here.

class products(models.Model):
    title = models.CharField(max_length=100)
    ref = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img/')
    price = models.IntegerField()
    url = models.URLField(blank=True)
    is_popular = models.BooleanField()
    is_underwear = models.BooleanField()
    is_sport = models.BooleanField()
    is_new = models.BooleanField()
    discontinued = models.BooleanField()