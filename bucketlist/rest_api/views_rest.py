# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from .models import Bucketlist, BucketListCategory, BucketListDetail
from .serializers import BucketlistSerializer, BucketlistCategorySerializer, BucketlistDetailSerializer


# api_rest/views
# The ListCreateAPIView is a generic view which provides GET (list all) and POST method handlers
# RetrieveUpdateDestroyAPIView is a generic view that provides GET(one), PUT, PATCH and DELETE method handlers.

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer


class CreateCategoryTypeView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = BucketListCategory.objects.all()
    serializer_class = BucketlistCategorySerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist category."""
        serializer.save()


class CategoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = BucketListCategory.objects.all()
    serializer_class = BucketlistCategorySerializer


class CreateBLDetailsView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = BucketListDetail.objects.all()
    serializer_class = BucketlistDetailSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist detail."""
        serializer.save()


class BLDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = BucketListCategory.objects.all()
    serializer_class = BucketlistDetailSerializer
