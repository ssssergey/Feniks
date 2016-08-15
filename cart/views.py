# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from django.template.loader import render_to_string, get_template
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from django.contrib.sites.shortcuts import get_current_site
from Feniks.settings import EMAIL_HOST_USER
# from forms import ContactForm
import cart
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from .forms import CheckoutForm
from .models import Order, OrderItem

from django.contrib import messages


def show_cart(request, template_name="cart/cart.html"):
    cart_item_count = cart.cart_item_count(request)
    if request.method == 'POST':
        postdata = request.POST.copy()
        print postdata
        if postdata['submit'] == u'Удалить':
            cart.remove_from_cart(request)
            message = u'Товар удален из корзины.'
            messages.success(request, message)
        if postdata['submit'] == u'Сохранить':
            cart.update_cart(request)
            message = u'Изменения приняты.'
            messages.success(request, message)
    cart_items = cart.get_cart_items(request)
    page_title = u'Корзина'
    cart_total = cart.cart_total(request)
    torgpred = False
    user = request.user
    if user.groups.filter(name=u'Торговые представители').exists():
        torgpred = True
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def confirm_order(request):
    user = request.user
    domain_url = ''.join(['http://', get_current_site(request).domain])
    cart_items = cart.get_cart_items(request)
    page_title = u'Подтверждение'
    cart_item_count = cart.cart_item_count(request)
    cart_total = cart.cart_total(request)
    form = CheckoutForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            # telephone_1 = form.cleaned_data['telephone_1']
            # email = form.cleaned_data['email']
            recipients = ['lse1983@mail.ru', 'feniks-kbr@yandex.ru']
            # Send email
            mail_template = 'mail/mail_order.html'
            # mail_txt = 'cart/mail.txt'
            # plaintext = get_template(mail_txt)
            # text_content = plaintext.render(d)
            context_dict_0 = {'cart_items': cart_items, 'cart_item_count': cart_item_count, 'cart_total': cart_total,
                              'domain_url': domain_url}
            context_dict = dict(context_dict_0.items() + form.cleaned_data.items())
            mail_theme = u'Тест - ЗАКАЗ'
            push_mail(context_dict, mail_theme, recipients, mail_template, False)
            # Clear Cart
            order = cart.create_order(request)
            if order.payment == u'Банковский перевод':
                schet = cart.create_schet(order)
                if order.email:
                    recipients = [order.email, ]
                    mail_template = 'cart/schet.html'
                    context_dict = {'schet': schet}
                    mail_theme = u'Тест - Счет для оплаты от магазина Феникс'
                    push_mail(context_dict, mail_theme, recipients, mail_template, True)
                return render_to_response("cart/schet.html",
                                          {'request': request, 'user': user, 'schet': schet})
            else:
                return render_to_response("cart/thanks.html",
                                          {'request': request, 'user': user})
    else:
        if request.user.is_authenticated():
            user = request.user
            data = {'last_name': user.last_name,
                    'first_name': user.first_name,
                    'patronymic': user.patronymic,
                    'email': user.email,
                    'telephone_1': user.telephone_1,
                    'country': user.country,
                    'region': user.region,
                    'city': user.city,
                    'adress': user.adress,
                    'index': user.index,
                    'skype': user.skype,
                    }
            form = CheckoutForm(initial=data)
    return render_to_response("cart/confirm.html", locals(), context_instance=RequestContext(request))


def push_mail(context_dict, mail_theme, recipients, mail_template, f_silent):
    # d = Context(context_dict)
    subject, from_email, to = mail_theme, EMAIL_HOST_USER, recipients
    htmly = get_template(mail_template)
    html_content = htmly.render(context_dict)
    text_content = render_to_string(mail_template, context_dict)
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send(fail_silently=f_silent)


################################# Checkout Views ########################################




# def show_checkout(request, template_name='checkout/checkout.html'):
#     if cart.is_empty(request):
#         cart_url = urlresolvers.reverse('show_cart')
#         return HttpResponseRedirect(cart_url)
#     if request.method == 'POST':
#         postdata = request.POST.copy()
#         form = CheckoutForm(postdata)
#         if form.is_valid():
#             response = checkout.process(request)
#             order_number = response.get('order_number', 0)
#             error_message = response.get('message', '')
#             if order_number:
#                 request.session['order_number'] = order_number
#                 receipt_url = urlresolvers.reverse('checkout_receipt')
#                 return HttpResponseRedirect(receipt_url)
#         else:
#             error_message = 'Correct the errors below'
#     else:
#         form = CheckoutForm()
#     page_title = 'Checkout'
#     return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def receipt(request, template_name='checkout/receipt.html'):
    order_number = request.session.get('order_number', '')
    if order_number:
        order = Order.objects.filter(id=order_number)[0]
        order_items = OrderItem.objects.filter(order=order)
        del request.session['order_number']
    else:
        cart_url = urlresolvers.reverse('show_cart')
        return HttpResponseRedirect(cart_url)
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))
