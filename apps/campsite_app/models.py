# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..log_reg_app.models import *
import datetime
from datetime import date

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=255)

class Activity(models.Model):
    name = models.CharField(max_length=255)

class CampsiteManager(models.Manager):
    def validator(self, postData, sessionUser):
        errors = {}
        # This currently validates (name, street, city, zip, and country string length), (long/lat value, long/lat still need to be validated that they convert successfully to a float), (request.session['user'] matches request.POST['uploader'])
        if str(sessionUser) != postData['uploader']:
            #This error currently reveals things about how we do logged in users
            errors['uploader'] = "The logged in user did not match the creator form"
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
        if float(postData['latitude']) > 90 or float(postData['latitude']) < -90:
            errors['latitude'] = "Latitude must be between -90 and 90"
        if float(postData['longitude']) > 180 or float(postData['longitude']) < -180:
            errors['longitude'] = "Longitude must be between -180 and 180"
        return errors
    def create_campsite(self, postData):
        name = postData['name']
        uploader = User.objects.get(id=int(postData['uploader']))
        address = postData['street'] + ";" + postData['city'] + ";" + postData['zip'] + ";" + postData['country']
        latitude = float(postData['latitude'])
        longitude = float(postData['longitude'])
        description = postData['description']
        open_date = datetime.date(2018, 1, 1)
        close_date = datetime.date(2018, 12, 31)
        if postData['no_max_nights'] == 'on':
            max_nights = "No max"
        else:
            max_nights = postData['max_nights']
        max_nights = postData['max_nights']
        number_of_sites = postData['number_of_sites']
        rv_length = postData['rv_length']
        road_conditions = postData['road_conditions']
        return Campsite.objects.create(
                name=name,
                uploader=uploader,
                address=address,
                latitude=latitude,
                longitude=longitude,
                description=description,
                open_date=open_date,
                close_date=close_date,
                max_nights=max_nights,
                number_of_sites=number_of_sites,
                rv_length=rv_length,
                road_conditions=road_conditions,
            )
    def add_services(self, postData, campsite):
        services = Service.objects.all()
        for service in services:
            key_string = "service_" + str(service.id)
            if postData[key_string] == 'on':
                campsite.services.add(service)
        return campsite
    def add_activities(self, postData, campsite):
        activities = Activity.objects.all()
        for activity in activities:
            key_string = "activity_" + str(activity.id)
            if postData[key_string] == 'on':
                campsite.activities.add(activity)
        return campsite

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