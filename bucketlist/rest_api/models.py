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
    topic = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    list_category = models.ForeignKey(BucketListCategory, on_delete=models.CASCADE)
    url = models.URLField(blank=True, null=True)
    dreamer = models.CharField(max_length=30, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.topic)


class BucketListDetail(models.Model):
    bucketlist = models.ForeignKey(Bucketlist, related_name='items', on_delete=models.CASCADE)
    vote = models.IntegerField(default=0)
    title = models.CharField(max_length=255, blank=True, null=True)
    priceMin = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    priceMax = models.DecimalField(max_digits=10, decimal_places=2, default=100000.00)
    reason = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    status = models.NullBooleanField(blank=True, null=True)
    date_target = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        verbose_name = 'BucketListDetail'
        verbose_name_plural = 'BucketListDetails'


# VALIDATORS
def isStatusValid(value):
    """
    Checks the validity of SystemData status field
    """
    valid_status_list = ['DEFAULT', 'NORMAL', 'NOT_AVAILABLE', 'NO_DEVICE', 'PROTOCOL_ERROR']
    isValid = False
    if value in valid_status_list:
        isValid = True

    return isValid


class DeviceProxy(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    ip_address = models.GenericIPAddressField()
    subnet_mask = models.GenericIPAddressField()
    port = models.IntegerField(default=47808)

    def __str__(self):
        return self.name + " (%s)" % self.ip_address


class SystemData(models.Model):
    identifier = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=64, unique=True)
    resolution = models.DecimalField(max_digits=3, decimal_places=3)
    unit = models.CharField(max_length=10)

    def __str__(self):
        return self.identfier + " : %s" % self.description


class SystemDataAcquisition(models.Model):
    # Delete all system data that belongs to deleted device proxy
    device_proxy = models.ForeignKey(DeviceProxy, on_delete=models.CASCADE)
    identifier = models.ForeignKey(SystemData, on_delete=models.CASCADE)

    timestamp = models.DateTimeField()
    status = models.CharField(max_length=32, validators=[isStatusValid])
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.identifier + " = %s %s" % (str(self.value), self.unit)
