# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from .models import Bucketlist, BucketListCategory, BucketListDetail


# rest_api/serializers.py

class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Bucketlist

        fields = ('id', 'topic', 'list_category', 'date_created', 'date_modified',
                  'items', 'url', 'dreamer', 'location', 'notes')
        read_only_fields = ('date_created', 'date_modified')


class BucketlistCategorySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = BucketListCategory

        fields = ('id', 'category', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class BucketlistDetailSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = BucketListDetail

        fields = ('id', 'bucketlist', 'title', 'vote', 'priceMin', 'priceMax', 'reason', 'notes',
                  'status', 'date_target', 'date_created', 'date_modified')

        read_only_fields = ('date_created', 'date_modified')