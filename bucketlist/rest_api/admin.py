# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Bucketlist, BucketListCategory, BucketListDetail
from .models import Profile, SystemData, DeviceProxy


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

    list_display = ('username',
                    'first_name',
                    'last_name',
                    'email',
                    'is_staff',
                    'get_role',
                    'get_location')

    list_select_related = ('profile',)

    def get_location(self, instance):
        return instance.profile.location

    def get_role(self, instance):
        return instance.profile.get_role_display()

    get_location.short_description = 'Location'
    get_role.short_description = 'Affiliation'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(SystemData)
admin.site.register(DeviceProxy)

class BucketListDetailInline(admin.StackedInline):
    model = BucketListDetail


class BucketListInline(admin.StackedInline):
    model = Bucketlist

@admin.register(Bucketlist)
class BucketlistAdmin(admin.ModelAdmin):
    inlines = [
        BucketListDetailInline
    ]

@admin.register(BucketListCategory)
class BucketCategoryAdmin(admin.ModelAdmin):
    inlines = [
        BucketListInline
    ]


    # TODO https://simpleisbetterthancomplex.com/tutorial/2017/03/14/how-to-create-django-admin-list-actions.html
