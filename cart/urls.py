from django.conf.urls import url

from views import show_cart, confirm_order

urlpatterns = [
    url(r'^$', show_cart, {'template_name': 'cart/cart.html'}, 'show_cart'),
    url(r'^confirm/$', confirm_order, {}, 'confirm_order'),
]
