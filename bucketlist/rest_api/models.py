# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# /rest_api/models.py

class Bucketlist(models.Model):
    """
    This class represents the bucketlist model.
    DEFAULT: id = models.AutoField(primary_key=True). This is an auto-incrementing primary key.
    If Django sees you’ve explicitly set Field.primary_key, it won’t add the automatic id column.
    """

    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
