# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Bucketlist, BucketListCategory, BucketListDetail


# api_rest/views
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_bucketlists = Bucketlist.objects.all().count()
    num_instances = BucketListDetail.objects.all().count()
    num_categories = BucketListCategory.objects.count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_bucketlists': num_bucketlists,
                 'num_instances': num_instances,
                 'num_categories': num_categories}
    )


def aboutme(request):
    #    Renders aboutme page html for sit author
    return render(request,
                  'aboutMe.html'
                  )
