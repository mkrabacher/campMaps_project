# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..campsite_app.models import *
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    sites = Campsite.objects.all()
    context = {
        'sites': sites
    }
    return render(request,'maps/index.html', context)