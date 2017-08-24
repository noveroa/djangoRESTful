# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import index, testScrapper, viewScrape, CreateWholeView, DetailsWholeView

# rest_api/urls.py

urlpatterns = {
    url(r'^$',
        index, name='index'),
    url(r'^scrape/(?P<start>[0-9]+)/(?P<end>[0-9]+)/$',
        testScrapper, name="testScrapper"),
    url(r'^viewPage/(?P<page>[0-9]+)/$',
        viewScrape, name="testScrapper"),
    url(r'^wholefoodrest/$',
        CreateWholeView.as_view(), name="createwholelist"),
    url(r'^wholefoodrest/(?P<pk>[0-9]+)/$',
        DetailsWholeView.as_view(), name="detailswhole"),

}

urlpatterns = format_suffix_patterns(urlpatterns)
