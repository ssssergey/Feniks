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
    price = models.IntegerField(null=True)

    class Meta:
        db_table = 'cart_items'
        ordering = ['date_added']

    def total(self):
        return self.quantity * self.price

    def name(self):
        return self.product.name

    # @property
    # def price(self):
    #     return self.product.price

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def augment_quantity(self, quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()


class Delivery(models.Model):
    name = models.CharField(u'Название', max_length=250, blank=True, unique=True)
    terminal = models.CharField(u'Терминал отправления', max_length=250, blank=True)
    site = models.CharField(u'Сайт', max_length=250, blank=True)
    number = models.IntegerField(u'Порядковый номер', default=0)

    class Meta:
        ordering = ['number', 'name']
        verbose_name = u'Способ доставки'
        verbose_name_plural = u'Способы доставки'

    def __unicode__(self):
        return self.name


class Order(models.Model):
    # each individual status
    CANCELLED = 0
    PROCESSED = 1
    SUBMITTED = 2
    PAYED = 3
    SHIPPED = 4
    COMPLETED = 5
    # set of possible order statuses
    ORDER_STATUSES = (
    (PROCESSED, u'В обработке'), (SUBMITTED, u'Принят'), (PAYED, u'Оплачен'), (SHIPPED, u'Отправлен'), (CANCELLED, u'Отменен'),
    (COMPLETED, u'Завершен'))
    # order info
    last_name = models.CharField(u'Фамилия', max_length=250)
    first_name = models.CharField(u'Имя', max_length=250)
    patronymic = models.CharField(u'Отчество', max_length=250, blank=True, null=True)
    date = models.DateTimeField(u'Создан', auto_now_add=True)
    status = models.IntegerField(u'Статус', choices=ORDER_STATUSES, default=PROCESSED)
    ip_address = models.GenericIPAddressField()
    last_updated = models.DateTimeField(u'Изменен', auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'Покупатель', null=True)
    # transaction_id = models.CharField(max_length=20)
    email = models.EmailField(u'Адрес электронной почты', max_length=250)
    telephone_1 = models.CharField(u'Номер телефона', max_length=20)
    country = models.CharField(u'Страна', max_length=250, default=u'Российская Федерация', null=True)
    region = models.CharField(u'Край, область, республика', max_length=250, blank=True, null=True)
    city = models.CharField(u'Населенный пункт', max_length=250, null=True, help_text=u'Например: г. Прохладный или с. Московское')
    adress = models.CharField(u'Улица, дом', max_length=250, null=True, help_text=u'Например: ул. Ленина 10 или пер. Красный 5')
    index = models.CharField(u'Почтовый индекс', max_length=250, null=True)
    skype = models.CharField(u'Скайп', max_length=250, blank=True, null=True)
    delivery = models.ForeignKey(Delivery, verbose_name=u'Способ доставки')
    # DELIVERY = (
    #     (u'Самовывоз', u'Самовывоз'),
    #     (u'ПЭК', u'ПЭК'),
    #     (u'Деловые линии', u'Деловые линии'),
    #     (u'Байкал сервис', u'Байкал сервис'),
    #     (u'Кит', u'Кит'),
    #     (u'Другой', u'Другой'),
    # )
    # delivery = models.CharField(u'Способ доставки', max_length=50, null=True, choices=DELIVERY, default=u'Самовывоз')

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
        return u'Заказ #{}'.format(self.id)

    @property
    def quantity(self):
        order_items = OrderItem.objects.filter(order=self)
        return len(order_items)

    @property
    def total(self):
        total = 0
        order_items = OrderItem.objects.filter(order=self)
        for item in order_items:
            total += item.total
        return total

    @models.permalink
    def get_absolute_url(self):
        return ('order_details', (), {'order_id': self.id})


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
        return u'Товар заказа: {}'.format(result)

    def get_absolute_url(self):
        return self.product.get_absolute_url()


class Schet(models.Model):
    platelshik = models.TextField(u'Плательшик', blank=True, null=True)
    gruzopoluchatel = models.TextField(u'Грузополучатель', blank=True, null=True)
    order = models.ForeignKey(Order, null=True)
    sum_price_words = models.TextField(u'Сумма словами', blank=True, null=True)
    date = models.DateTimeField(u'Создан', auto_now_add=True)

    class Meta:
        verbose_name = u'Счет'
        verbose_name_plural = u'Счета'

    @property
    def nds(self):
        float_total = self.order.total * 0.18
        return "{0:.2f}".format(round(float_total, 2))

    def __unicode__(self):
        return u'Счет №: {}'.format(self.id)

