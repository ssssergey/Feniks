# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from catalog.models import Product
from Feniks import settings


class PageView(models.Model):
    class Meta:
        abstract = True

    date = models.DateTimeField(auto_now=True)
    ip_address = models.GenericIPAddressField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    tracking_id = models.CharField(max_length=50, default='')


class ProductView(PageView):
    product = models.ForeignKey(Product)
