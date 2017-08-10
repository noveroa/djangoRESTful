# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist

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