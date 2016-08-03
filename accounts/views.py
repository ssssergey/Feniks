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
    print(request.user.is_authenticated())
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


@login_required
def my_account(request, template_name="registration/my_account.html"):
    page_title = u'Личный кабинет'
    orders = Order.objects.filter(user=request.user)
    name = request.user.username
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
