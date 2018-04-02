from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.


class AppUser(models.Model):

    name = models.TextField()
    course = models.TextField()
    enrollmentno = models.TextField()
    year = models.IntegerField()
    detailforappointment = models.TextField(default='')
    timestamp = models.DateField()

    def __str__():
        return self.name	
