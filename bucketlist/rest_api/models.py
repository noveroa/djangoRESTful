# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# /rest_api/models.py


class Profile(models.Model):
    VISITOR = 1
    COLLEAGUE = 2
    SUPERUSER = 3
    role_choices = (
        (VISITOR, 'Visitor'),
        (COLLEAGUE, 'Colleague'),
        (SUPERUSER, 'Superuser'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=role_choices, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class BucketListCategory(models.Model):
    category = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.category)

    class Meta:
        verbose_name = 'BucketListCategory'
        verbose_name_plural = 'BucketListCategories'

class Bucketlist(models.Model):
    """
    This class represents the bucketlist model.
    DEFAULT: id = models.AutoField(primary_key=True). This is an auto-incrementing primary key.
    If Django sees you’ve explicitly set Field.primary_key, it won’t add the automatic id column.
    """

    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    list_category = models.ForeignKey(BucketListCategory, on_delete=models.CASCADE)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class BucketListDetail(models.Model):
    name = models.OneToOneField(Bucketlist, on_delete=models.CASCADE)
    dreamer = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField(blank=True, null=True)
    status = models.NullBooleanField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'BucketListDetail'
        verbose_name_plural = 'BucketListDetails'
