# -*- coding: utf-8 -*-
from forms import UserLoginForm, UserRegisterForm
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect, render
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
import profile

# # CUSTOM REGISTER VIEW
# def register(request, template_name="registration/register.html"):
#     if request.method == 'POST':
#         postdata = request.POST.copy()
#         form = RegisterForm(postdata)
#         if form.is_valid():
#             form.save()
#             un = postdata.get('username', '')
#             pw = postdata.get('password1', '')
#             new_user = authenticate(username=un, password=pw)
#             if new_user and new_user.is_active:
#                 login(request, new_user)
#                 url = urlresolvers.reverse('catalog_home')
#                 return HttpResponseRedirect(url)
#     else:
#         form = RegisterForm()
#     page_title = u'Регистрация пользователя'
#     return render_to_response(template_name, locals(), context_instance=RequestContext(request))


# ALTERNATIVE CUSTOM REGISTER VIEW
def register_view(request, template_name="registration/register.html"):
    page_title = u'Регистрация'
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('/')
    context = {'form': form, 'title': page_title}
    return render(request, "registration/register.html", context)


# CUSTOM LOGIN
def login_view(request):
    print(request.user.is_authenticated())
    page_title = u"Вход"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    return render(request, "registration/login.html", {"form": form, "page_title": page_title})


# CUSTOM LOGOUT
def logout_view(request):
    logout(request)
    return render(request, "catalog/index.html", {})


from cart.models import Order, OrderItem
from django.contrib.auth.decorators import login_required

from django.db import connection
from django.db.models.aggregates import Count, Sum
import time
from django.db.models import Q


@login_required
def my_account(request, template_name="registration/my_account.html"):
    name = request.user.get_full_name()
    page_title = u'Личный кабинет'
    orders = Order.objects.filter(user=request.user)
    torgpred = False
    user = request.user
    if user.groups.filter(name=u'Торговые представители').exists():
        torgpred = True
        data = {}
        user_oi_qs = OrderItem.objects.filter(order__user=user)
        user_oi_qs_processed = user_oi_qs.filter(order__status=1)
        user_oi_qs_submitted = user_oi_qs.filter(order__status=2)
        user_oi_qs_shipped = user_oi_qs.filter(order__status=3)
        user_oi_qs_completed = user_oi_qs.filter(order__status=4)
        user_oi_qs_canceled = user_oi_qs.filter(order__status=0)
        x = 6
        now = time.localtime()
        last_months = [time.localtime(time.mktime((now.tm_year, now.tm_mon - n, 1, 0, 0, 0, 0, 0, 0)))[:2] for n in range(x)]
        # [(2016, 8), (2016, 7), (2016, 6), (2016, 5), (2016, 4), (2016, 3), (2016, 2), (2016, 1), (2015, 12), (2015, 11)]
        data = []
        for couple in last_months:
            month_obj = {
                'month':couple,
                'products_aggregated': [],
                'product_items': [],
                'month_total': 0,
                'month_margin': 0,
            }
            month_oi_qs = user_oi_qs_completed.filter(order__date__year=couple[0], order__date__month=couple[1])
            distinct_product_oi_qs = month_oi_qs.distinct('product')

            # for i in distinct_product_oi_qs:
            #     product_sum = month_oi_qs.filter(Q(product=i.product)).aggregate(Sum("quantity"))
            #     month_obj['products_aggregated'].append((i.product, product_sum))

            for p in month_oi_qs:
                month_obj['month_total'] += p.total
                p.margin = p.price-p.product.price_bulk1
                month_obj['month_margin'] += p.margin
                month_obj['product_items'].append(p)
            month_obj['percent'] = 0
            if month_obj['month_total'] < 100000:
                month_obj['percent'] = 20
            elif month_obj['month_total'] > 100000 and month_obj['month_total'] < 500000:
                month_obj['percent'] = 40
            elif month_obj['month_total'] > 500000 and month_obj['month_total'] < 1000000:
                month_obj['percent'] = 60
            elif month_obj['month_total'] > 1000000 and month_obj['month_total'] < 2000000:
                month_obj['percent'] = 80
            elif month_obj['month_total'] > 2000000:
                month_obj['percent'] = 100
            month_obj['profit'] = month_obj['month_margin']/100  * month_obj['percent']
            data.append(month_obj)
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


@login_required
def order_details(request, order_id, template_name="registration/order_details.html"):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    page_title = u'Подробнее о Заказе #' + order_id
    order_items = OrderItem.objects.filter(order=order)
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


@login_required
def order_info(request, template_name="registration/order_info.html"):
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = UserRegisterForm(postdata)
        if form.is_valid():
            profile_form = UserRegisterForm(request.POST, instance=request.user)
            profile_form.save()
            url = urlresolvers.reverse('my_account')
            return HttpResponseRedirect(url)
    else:
        user_profile = request.user
        form = UserRegisterForm(instance=user_profile)
    page_title = u'Редактирование регистрационных данных'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))
