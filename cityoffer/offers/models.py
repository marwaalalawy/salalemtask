# from django.db import models


from __future__ import unicode_literals

from django.db import models
import datetime
# Create your models here.

class Offer(models.Model):
    companyName=models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    date=models.CharField(max_length=200)
    
    location=models.CharField(max_length=200)

    def __str__(self):
     	  return self.descriptions