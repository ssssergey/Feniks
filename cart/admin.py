# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Order, OrderItem, Delivery


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'date', 'status', 'id', 'user')
    list_filter = ('status', 'date')
    search_fields = ('email', 'delivery', 'payment', 'id')
    inlines = [OrderItemInline, ]
    fieldsets = (
        (u'Главное', {'fields': ('last_name', 'first_name', 'patronymic', 'status', 'email', 'telephone_1')}),
        (u'Доставка и оплата', {'fields': ('payment', 'delivery', 'adress', 'city', 'region', 'index', 'country')})
    )


admin.site.register(Order, OrderAdmin)


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('name', 'terminal', 'site')

admin.site.register(Delivery, DeliveryAdmin)