# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from models import *
import bcrypt, random

# Create your views here.
def index(request):
    if 'user' in request.session:
        return redirect('/')
    return render(request, "log_reg_app/index.html")

def process_reg(request):
    if request.method == "POST":
        errors = User.objects.reg_valid(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/login')
        else:
            name = request.POST['name']
            username = request.POST['username']
            email = request.POST['email']
            hashed_pass = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(name=name, username=username, password=hashed_pass, email=email)
            request.session['user'] = user.id
            return redirect('/')
    return redirect('/login')

def process_log(request):
    if request.method == "POST":
        errors = User.objects.log_valid(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/login')
        else:
            user = User.objects.get(username=request.POST['username'])
            request.session['user'] = user.id
            return redirect('/')
    return redirect('/login')

def process_logout(request):
    if request.method == "POST":
        request.session.clear()
        return redirect('/login')
    return redirect('/login')