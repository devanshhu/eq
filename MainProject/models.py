from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.


class AppUser(models.Model):

    name = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    enrollmentno = models.CharField(max_length=20)
    year = models.IntegerField()
    detailforappointment = models.TextField(default='')
    timestamp = models.DateField()

    def __str__():
        return self.name
