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
    return render(request, 'campsite_app/site.html')

def site_id(request, id):
    try:
        context = {
            'site': Campsite.objects.get(id=id)
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
        errors = Campsite.objects.validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/site/add')
        else:
            pass
    return redirect('/')