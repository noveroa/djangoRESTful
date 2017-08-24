# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse
from rest_framework import generics

from .models import WholeFoodsStore
from .scraper import *
from .serializers import WholeFoodsStoreSerializer


# Create your views here.
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects

    return HttpResponse("You're at wholefoods")


def testScrapper(request, start, end, save=True):
    wfscraper = WholeFoodsScraper()
    wfscraper.run(start, end, save)

    return HttpResponse(wfscraper.open_data())


def viewScrape(request, page, save=False):
    print save
    wfscraper = WholeFoodsScraper()
    page = int(page)
    wfscraper.run(page, page + 1, save)

    return HttpResponse(wfscraper.open_data())


class CreateWholeView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = WholeFoodsStore.objects.all()
    serializer_class = WholeFoodsStoreSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class DetailsWholeView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = WholeFoodsStore.objects.all()
    serializer_class = WholeFoodsStoreSerializer
