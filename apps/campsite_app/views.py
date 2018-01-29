# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *
from ..log_reg_app.models import *

# Create your views here.
def site(request):
    return render(request, 'campsite_app/site.html')

def site_id(request, number):
    try:
        context = {
            'site': Campsite.objects.get(id=number)
        }
        return render(request, 'campsite_app/site_id.html', context)
    except:
        return redirect('/')