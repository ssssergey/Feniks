from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^results/$',results,{'template_name': 'search/results.html'}, 'search_results'),
    url(r'^review/product/add/$', add_review),
]