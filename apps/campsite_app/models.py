# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..log_reg_app.models import *

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=255)

class Amenity(models.Model):
    name = models.CharField(max_length=255)

class CampsiteManager(models.Manager):
    def validator(self, postData):
        errors = {}
        # Validations for adding a campsite go here
        return errors

class Campsite(models.Model):
    name = models.CharField(max_length=255)
    uploader = models.ForeignKey(User, related_name='created_campsites')
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField()
    activities = models.ManyToManyField(Amenity)
    services = models.ManyToManyField(Service)
    open_date = models.DateField()
    close_date = models.DateField()
    max_nights = models.CharField(max_length=10)
    rv_length = models.CharField(max_length=20)
    road_conditions = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CampsiteManager()