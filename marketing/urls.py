from marketing.sitemap import SITEMAPS
from django.conf.urls import url
from .views import robots

urlpatterns = [
    url(r'^robots\.txt$', robots),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': SITEMAPS}),
]
