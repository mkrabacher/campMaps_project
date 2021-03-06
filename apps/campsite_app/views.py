# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core import serializers
from models import *
from ..log_reg_app.models import *
import requests

# Create your views here.
def index(request):
    sites = Campsite.objects.all()
    context = {
        'sites': sites
    }
    return render(request,'campsite_app/index.html', context)

def user(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'campsite_app/user.html', context)

def about(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'campsite_app/about.html', context)

def user_id(request, id):
    try: 
        user = User.objects.get(id=id)
        sites = Campsite.objects.filter(uploader=user)
        context = {
            'user': user,
            'sites': sites
        }
        return render(request, 'campsite_app/user_id.html', context)
    except:
        return redirect('/')

def site(request):
    context = {
        'campsites': Campsite.objects.all()
    }
    return render(request, 'campsite_app/site.html', context)

def site_id(request, id):
    try:
        campsite = Campsite.objects.get(id=id)
    except:
        return redirect('/site')
    # Weather API backend call starts here
    #
    # Weather API backend call ends here
    services = Service.objects.filter(campsite=campsite)
    activities = Activity.objects.filter(campsite=campsite)
    context = {
            'campsite': Campsite.objects.get(id=id),
            'services': services,
            'activities': activities
        }
    return render(request, 'campsite_app/site_id.html', context)

def get_weather(request, latlng):
    print 'latlng below'
    print latlng
    url = "https://api.darksky.net/forecast/6f2ceccdc4c5425df7336b58b16618bd/" + latlng
    response = requests.get(url).content
    print 'response below'
    print response
    return HttpResponse(response, content_type='application/json')

def site_add(request):
    if 'user' in request.session:
        context = {
            'services': Service.objects.all(),
            'activities': Activity.objects.all()
        }
        return render(request, 'campsite_app/site_add.html', context)
    else:
        messages.error(request, 'You must be logged in to create a campsite')
        return redirect('/login')

def process_add(request):
    if request.method == "POST":
        errors = Campsite.objects.validator(request.POST, request.session['user'])
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/site/add')
        else:
            campsite = Campsite.objects.create_campsite(request.POST)
            Campsite.objects.add_activities(request.POST, campsite)
            Campsite.objects.add_services(request.POST, campsite)
            target_string = "/site/" + str(campsite.id)
            return redirect(target_string)
    return redirect('/')

def sites_json(request):
    sites = Campsite.objects.all()
    return HttpResponse(serializers.serialize("json", sites), content_type="application/json")

def json_test(request):
    return render(request, 'campsite_app/json_test.html')
