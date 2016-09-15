from marketing.sitemap import SITEMAPS
from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from .views import robots

urlpatterns = [
    url(r'^robots\.txt$', robots),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': SITEMAPS}),
]
