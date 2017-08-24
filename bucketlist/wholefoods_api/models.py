# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class WholeFoodsStore(models.Model):
    storeid = models.IntegerField(blank=True, null=True)
    hours = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    locality = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.PositiveIntegerField(blank=True, null=True)
    store_image = models.URLField(max_length=255, blank=True, null=True)
