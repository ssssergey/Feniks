# -*- coding: utf-8 -*-

from .models import CartItem, Schet
from catalog.models import Product
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

import random

from django.conf import settings
from django.db.models import Max
from Feniks.settings import SESSION_AGE_DAYS
from datetime import datetime, timedelta
from myutils.num2t4ru import num2text


CART_ID_SESSION_KEY = 'cart_id'
# get the current user's cart id, sets new one if blank
def _cart_id(request):
    if request.session.get(CART_ID_SESSION_KEY, '') == '':
        request.session[CART_ID_SESSION_KEY] = _generate_cart_id()
    return request.session[CART_ID_SESSION_KEY]


def _generate_cart_id():
    cart_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    cart_id_length = 50
    for y in range(cart_id_length):
        cart_id += characters[random.randint(0, len(characters) - 1)]
    return cart_id


# return all items from the current user's cart
def get_cart_items(request):
    return CartItem.objects.filter(cart_id=_cart_id(request))

def is_empty(request):
    return cart_item_count(request) == 0

def empty_cart(request):
    user_cart = get_cart_items(request)
    user_cart.delete()

# add an item to the cart
def add_to_cart(request):
    postdata = request.POST.copy()
    # get product slug from post data, return blank if empty
    product_slug = postdata.get('product_slug', '')
    # get quantity added, return 1 if empty
    quantity = postdata.get('quantity', 1)
    # fetch the product or return a missing page error
    p = get_object_or_404(Product, slug=product_slug)
    # print "Was {}".format(p.quantity)
    # get products in cart
    cart_products = get_cart_items(request)
    product_in_cart = False
    # check to see if item is already in cart
    for cart_item in cart_products:
        if cart_item.product.id == p.id:
            # update the quantity if found
            cart_item.augment_quantity(quantity)
            product_in_cart = True
    if not product_in_cart:
        # create and save a new cart item
        ci = CartItem()
        ci.product = p
        ci.quantity = quantity
        ci.price = p.price
        ci.cart_id = _cart_id(request)
        ci.save()
    # p.quantity -= int(quantity)
    # p.save()
    # print "Now {}".format(p.quantity)
    # returns the total number of items in the user's cart


def cart_distinct_item_count(request):
    return get_cart_items(request).count()


def cart_item_count(request):
    return get_cart_items(request).count()


def get_single_item(request, item_id):
    return get_object_or_404(CartItem, id=item_id, cart_id=_cart_id(request))


# update quantity for single item
def update_cart(request):
    postdata = request.POST.copy()
    item_id = postdata['item_id']
    quantity = postdata['quantity']
    price = postdata['price']
    cart_item = get_single_item(request, item_id)
    cart_item.price = int(price)
    cart_item.save()
    if cart_item:
        if int(quantity) > 0:
            # delta_quantity = int(quantity) - cart_item.quantity
            cart_item.quantity = int(quantity)
            cart_item.save()
            # product = Product.active.get(cartitem=cart_item)
            # print "Was {}".format(product.quantity)
            # product.quantity -= delta_quantity
            # product.save()
            # print "Now {}".format(product.quantity)
        else:
            remove_from_cart(request)


# remove a single item from cart
def remove_from_cart(request):
    postdata = request.POST.copy()
    item_id = postdata['item_id']
    cart_item = get_single_item(request, item_id)
    if cart_item:
        # product = Product.active.get(cartitem=cart_item)
        # print "Was {}".format(product.quantity)
        # product.quantity += cart_item.quantity
        # product.save()
        # print "Now {}".format(product.quantity)
        cart_item.delete()

from django.contrib import messages
def remove_from_orders(request):
    postdata = request.POST.copy()
    item_id = postdata['order_id']
    order = get_object_or_404(Order, id=item_id)
    if order and order.status == 1:
        order.delete()
        message = u'Заказ удален.'
        messages.success(request, message)
    else:
        message = u'Вы не можете удалить этот заказ.'
        messages.warning(request, message)

# gets the total cost for the current cart
def cart_total(request):
    cart_total = 0
    cart_products = get_cart_items(request)
    for cart_item in cart_products:
        cart_total += cart_item.price * cart_item.quantity
    return cart_total


def remove_old_cart_items():
    print "Removing old carts"
    # calculate date of SESSION_AGE_DAYS days ago
    remove_before = datetime.now() + timedelta(days=-settings.SESSION_AGE_DAYS)
    cart_ids = []
    old_items = CartItem.objects.values('cart_id').annotate(last_change=Max('date_added')).filter(
        last_change__lt=remove_before).order_by()
    # create a list of cart IDs that haven’t been modified
    for item in old_items:
        cart_ids.append(item['cart_id'])
    to_remove = CartItem.objects.filter(cart_id__in=cart_ids)
    # delete those CartItem instances
    to_remove.delete()
    print str(len(cart_ids)) + " carts were removed"

################################# Checkout Views ########################################

from .models import Order, OrderItem
from .forms import CheckoutForm
from django.core import urlresolvers

# returns the URL from the checkout module for cart
def get_checkout_url(request):
    return urlresolvers.reverse('checkout')


def create_order(request):
    order = Order()
    checkout_form = CheckoutForm(request.POST, instance=order)
    order = checkout_form.save(commit=False)
    # order.transaction_id = order.id
    order.ip_address = request.META.get('REMOTE_ADDR')
    order.user = None
    if request.user.is_authenticated():
        order.user = request.user
    order.status = Order.PROCESSED
    order.save()
    # if the order save succeeded
    if order.pk:
        cart_items = get_cart_items(request)
        for ci in cart_items:
            # create order item for each cart item
            oi = OrderItem()
            oi.order = order
            oi.quantity = ci.quantity
            oi.price = ci.price  # now using @property
            oi.product = ci.product
            oi.save()
        # all set, empty cart
        empty_cart(request)
    # # save profile info for future orders
    # if request.user.is_authenticated():
    #     from accounts import profile
    #     profile.set(request)
    # return the new order object
    return order



def create_schet(order):
    schet = Schet()
    schet.order = order
    schet.platelshik = u'{} {}'.format(order.last_name, order.first_name)
    schet.gruzopoluchatel = u'{} {}'.format(order.last_name, order.first_name)
    schet.sum_price_words = num2text(order.total)
    schet.save()
    return schet