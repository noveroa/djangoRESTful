# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from .models import WholeFoodsStore


# rest_api/serializers.py


class WholeFoodsStoreSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = WholeFoodsStore

        fields = ('storeid', 'hours', 'phone', 'name', 'locality',
                  'state', 'zipcode', 'store_image')

        read_only_fields = ('storeid', 'hours', 'phone', 'name', 'locality',
                            'state', 'zipcode', 'store_image')
