from django.db import models

class Regions(models.Model):
    regions_name = models.CharField(max_length=100)
    regions_ref = models.CharField(max_length=100)



class Tenants(models.Model):
    tenants_name = models.CharField(max_length=100)
    tenants_ref = models.CharField(max_length=100)
    regionz = models.ManyToManyField(Regions)

class NameSpaces(models.Model):
    namespaces_name = models.CharField(max_length=100)
    namespaces_ref = models.CharField(max_length=100)
    tenantz = models.ManyToManyField(Tenants)

