# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from catalog.models import Product
from django.core.urlresolvers import reverse
from Feniks import settings
from django import forms

# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType
#     content_type = models.ForeignKey(ContentType)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')

class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey('catalog.Product', unique=False, null=True)

    class Meta:
        db_table = 'cart_items'
        ordering = ['date_added']

    def total(self):
        return self.quantity * self.product.price

    def name(self):
        return self.product.name

    @property
    def price(self):
        return self.product.price

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def augment_quantity(self, quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()


class Order(models.Model):
    # each individual status
    PROCESSED = 1
    SUBMITTED = 2
    SHIPPED = 3
    CANCELLED = 4
    COMPLETED = 5
    # set of possible order statuses
    ORDER_STATUSES = ((PROCESSED, u'В обработке'), (SUBMITTED, u'Принят'), (SHIPPED, u'Отправлен'), (CANCELLED, u'Отменен'),
                      (COMPLETED, u'Завершен'))
    # order info
    last_name = models.CharField(u'Фамилия', max_length=50)
    first_name = models.CharField(u'Имя', max_length=50)
    patronymic = models.CharField(u'Отчество', max_length=50, blank=True, null=True)
    date = models.DateTimeField(u'Создан', auto_now_add=True)
    status = models.IntegerField(u'Статус', choices=ORDER_STATUSES, default=PROCESSED)
    ip_address = models.GenericIPAddressField()
    last_updated = models.DateTimeField(u'Изменен', auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    # transaction_id = models.CharField(max_length=20)
    email = models.EmailField(u'Адрес электронной почты', max_length=50)
    telephone_1 = models.CharField(u'Номер телефона', max_length=20)
    country = models.CharField(u'Страна', max_length=50, default=u'Российская Федерация', null=True)
    region = models.CharField(u'Край, область, республика', max_length=50, blank=True, null=True)
    city = models.CharField(u'Город', max_length=50, blank=True, null=True)
    adress = models.CharField(u'Улица, дом', max_length=100, blank=True, null=True)
    index = models.CharField(u'Почтовый индекс', max_length=10, blank=True, null=True)
    skype = models.CharField(u'Скайп', max_length=50, blank=True, null=True)

    DELIVERY = (
        (u'Самовывоз', u'Самовывоз'),
        (u'ПЭК', u'ПЭК'),
        (u'Деловые линии', u'Деловые линии'),
        (u'Байкал сервис', u'Байкал сервис'),
        (u'Кит', u'Кит'),
        (u'Другой', u'Другой'),
    )
    delivery = models.CharField(u'Способ доставки', max_length=50, null=True, choices=DELIVERY, default=u'Самовывоз')
    PAYMENT = (
        (u'Наличные', u'Наличные'),
        (u'Банковский перевод', u'Банковский перевод'),
        (u'Банковская карта', u'Банковская карта'),
        (u'Другой', u'Другой'),
    )
    payment = models.CharField(u'Способ оплаты', max_length=50, null=True, choices=PAYMENT, default=u'Наличные')

    class Meta:
        verbose_name = u'Заказ'
        verbose_name_plural = u'Заказы'

    def __unicode__(self):
        return u'Заказ #' + str(self.id)

    @property
    def total(self):
        total = 0
        order_items = OrderItem.objects.filter(order=self)
        for item in order_items:
            total += item.total
        return total

    @models.permalink
    def get_absolute_url(self):
        return ('order_details', (), { 'order_id': self.id })


class OrderItem(models.Model):
    product = models.ForeignKey(Product, verbose_name=u'Товар')
    quantity = models.IntegerField(u'Количество', default=1)
    price = models.IntegerField(u'Цена')
    order = models.ForeignKey(Order)

    class Meta:
        verbose_name = u'Позиция заказа'
        verbose_name_plural = u'Позиции заказа'

    @property
    def total(self):
        return self.quantity * self.price

    @property
    def name(self):
        return self.product.name

    @property
    def sku(self):
        return self.product.sku

    def __unicode__(self):
        if self.product.sku:
            result = self.product.name + ' (' + self.product.sku + ')'
        else:
            result = self.product.name
        return result

    def get_absolute_url(self):
        return self.product.get_absolute_url()
