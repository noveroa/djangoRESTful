# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import WholeFoodsStore


# Register your models here.
@admin.register(WholeFoodsStore)
class WholeFoodsStoreAdmin(admin.ModelAdmin):
    pass
