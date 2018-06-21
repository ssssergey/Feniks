from django.conf.urls import url
from views import register_view, my_account, order_info, order_details
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^register/$', register_view, {'template_name': 'registration/register.html'}, 'register'),
    url(r'^my_account/$', my_account, {'template_name': 'registration/my_account.html'}, 'my_account'),
    url(r'^order_details/(?P<order_id>[-\w]+)/$', order_details, {'template_name': 'registration/order_details.html'},
        'order_details'),
    url(r'^order_info//$', order_info, {'template_name': 'registration/order_info.html'}, 'order_info'),
    url(r'^login/$', login, {'template_name': 'registration/login.html'}, 'login'),
]
