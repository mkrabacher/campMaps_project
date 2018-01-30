# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..log_reg_app.models import *

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=255)

class Activity(models.Model):
    name = models.CharField(max_length=255)

class CampsiteManager(models.Manager):
    def validator(self, postData):
        errors = {}
        # Validations for adding a campsite go here
        if len(postData['name']) < 3:
            errors['name'] = "Names must be 3 or more characters"
        if len(postData['street']) < 2:
            errors['street'] = "Street must be 2 or more characters"
        if len(postData['city']) < 2:
            errors['city'] = "City name must be 2 or more characters"
        if len(postData['zip']) != 5:
            errors['zip'] = "Zip codes must be 5 digits"
        if len(postData['country']) < 4:
            errors['country'] = "Country names must be 4 or more characters"
        if float(postData['longitude']) > 90 or float(postData['longitude']) < -90:
            errors['longitude'] = "Longitude must be between -90 and 90"
        if float(postData['latitude']) > 180 or float(postData['latitude']) < -180:
            errors['latitude'] = "Latitude must be between -180 and 180"
        return errors

class Campsite(models.Model):
    name = models.CharField(max_length=255)
    uploader = models.ForeignKey(User, related_name='created_campsites')
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField()
    activities = models.ManyToManyField(Activity)
    services = models.ManyToManyField(Service)
    open_date = models.DateField()
    close_date = models.DateField()
    max_nights = models.CharField(max_length=10)
    number_of_sites = models.CharField(max_length=10)
    rv_length = models.CharField(max_length=20)
    road_conditions = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CampsiteManager()