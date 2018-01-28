# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def reg_valid(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['name']) < 3:
            errors['name'] = "Names must be 3 or more characters"
        if len(postData['username']) < 3:
            errors['username'] = "Usernames must be 3 or more characters"
        else:
            try:
                User.objects.get(username=postData['username'])
                errors['username'] = "Username is already in use"
            except:
                pass
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email must be valid"
        else:
            try:
                User.objects.get(email=postData['email'])
                errors['email'] = "Email is already in use"
            except:
                pass
        if len(postData['password']) < 8:
            errors['password'] = "Passwords must be 8 or more characters"
        if postData['password'] != postData['r_password']:
            errors['r_password'] = "Password fields must match"
        return errors

    def log_valid(self, postData):
        errors = {}
        try:
            user = User.objects.get(username=postData['username'])
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors['password'] = "Invalid password"
        except:
            errors['username'] = "That username is not in use"
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()