from django.db import models
from datetime import datetime
from realtors.models import Realtor #From Realtor build relation to database

# Create your models here.
class Listing(models.Model): #class <First Capital> Listing
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    district = models.CharField(max_length=50) # 50 chars
    description = models.TextField(blank=True) # 200 wordings
    price = models.IntegerField() #Integer
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    clubhouse = models.IntegerField()
    sqft = models.IntegerField()
    estate_size = models.FloatField(default=0.0) #Float
    is_published = models.BooleanField(default=True) #Boolean
    list_date = models.DateTimeField(auto_now_add=True) #DateTime
    photo_main = models.ImageField(upload_to='photo/%Y/%m/%d/') #Image
    photo_1 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    
    def __str__(self):
        return self.title