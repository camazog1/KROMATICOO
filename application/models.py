from django.db import models

# Create your models here.

class products(models.Model):
    title = models.CharField(max_length=100)
    ref = models.CharField(max_length=100, primary_key=True)
    desc = models.CharField(max_length=1000)
    price = models.IntegerField()
    price_dolar = models.DecimalField(max_digits=10, decimal_places=2)
    img1 = models.ImageField(upload_to='img/')
    img2 = models.ImageField(upload_to='img/')
    img3 = models.ImageField(upload_to='img/')
    img4 = models.ImageField(upload_to='img/')
    is_popular = models.BooleanField()
    is_underwear = models.BooleanField()
    is_sport = models.BooleanField()
    is_new = models.BooleanField()
    discontinued = models.BooleanField()