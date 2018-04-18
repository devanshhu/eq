from django.db import models
from django import forms
from datetime import date
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.


class AppUser(models.Model):

    name = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    enrollmentno = models.CharField(max_length=20)
    year = models.IntegerField()
    detailforappointment = models.CharField(max_length=200)
    regdate = models.DateField(blank=True, null=True)
    timestamp = models.DateField(blank=True, null=True)
    timeslot_start = models.DateField(blank=True, null=True)
    timeslot_end = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
