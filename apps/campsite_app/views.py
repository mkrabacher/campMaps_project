# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from models import *
from ..log_reg_app.models import *

# Create your views here.
def user_id(request, id):
    try:
        user = User.objects.get(id=id)
        context = {
            'user': user
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
        context = {
            'campsite': Campsite.objects.get(id=id)
        }
        return render(request, 'campsite_app/site_id.html', context)
    except:
        return redirect('/')

def site_add(request):
    if 'user' in request.session:
        context = {
            'services': Service.objects.all(),
            'activities': Activity.objects.all()
        }
        return render(request, 'campsite_app/site_add.html', context)
    else:
        #add message informing the user that they must be logged in to add a campsite
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
            target_string = "/site/" + str(campsite.id)
            return redirect(target_string)
    return redirect('/')