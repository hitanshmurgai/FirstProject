from django.db import models
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(max_length=255)


class JobDetails(models.Model):
    jobtitle = models.CharField(max_length=255)
    jobdesc = models.CharField(max_length=600)
    jobofficer = models.CharField(max_length=255)
    jobdetails = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_on = models.DateField(default=timezone.now)


# Create your models here.
