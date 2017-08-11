# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import index, aboutme
from .views_rest import CreateBLDetailsView, BLDetailsView
from .views_rest import CreateCategoryTypeView, CategoryDetailsView
from .views_rest import CreateView, DetailsView

# rest_api/urls.py

urlpatterns = {
    url(r'^$',
        index, name='index'),
    url(r'^aboutMe/$',
        aboutme, name='aboutMe'),
    url(r'^bucketlists/$',
        CreateView.as_view(), name="createlist"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details"),
    url(r'^bucketlistcategories/$',
        CreateCategoryTypeView.as_view(), name="createcategory"),
    url(r'^bucketlistcategories/(?P<pk>[0-9]+)/$',
        CategoryDetailsView.as_view(), name="details"),
    url(r'^bucketlistdetails/$',
        CreateBLDetailsView.as_view(), name="createdetail"),
    url(r'^bucketlistdetails/(?P<pk>[0-9]+)/$',
        BLDetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)