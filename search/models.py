# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from Feniks import settings
from catalog.models import Product


class SearchTerm(models.Model):
    q = models.CharField(u'Поисковая фраза', max_length=50)
    search_date = models.DateTimeField(u'Когда искали', auto_now_add=True)
    ip_address = models.GenericIPAddressField(u'IP-адрес')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, verbose_name=u'Пользователь')
    tracking_id = models.CharField(max_length=50, default='')

    class Meta:
        ordering = ['-search_date']
        verbose_name = u'Поисковый запрос'
        verbose_name_plural = u'Поисковые запросы'

    def __unicode__(self):
        return self.q


class Faq(models.Model):
    question = models.CharField(u'Вопрос', max_length=255, blank=True, unique=True)
    answer = models.TextField(u'Ответ', blank=True, unique=True)

    class Meta:
        verbose_name = u'Вопросы и ответы'
        verbose_name_plural = u'Вопросы и ответы'

    def __unicode__(self):
        return u'Вопрос №{}'.format(self.id)


class ActiveProductReviewManager(models.Manager):
    def all(self):
        return super(ActiveProductReviewManager, self).all().filter(is_approved=True)


class ProductReview(models.Model):
    RATINGS = ((5, 5), (4, 4), (3, 3), (2, 2), (1, 1),)
    product = models.ForeignKey(Product, verbose_name=u'Товар')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'Пользователь')
    date = models.DateTimeField(u'Создан', auto_now_add=True)
    rating = models.PositiveSmallIntegerField(u'Рейтинг', default=5, choices=RATINGS)
    is_approved = models.BooleanField(u'Одобрен', default=True)
    content = models.TextField(u'Текст')
    objects = models.Manager()
    approved = ActiveProductReviewManager()

    class Meta:
        verbose_name = u'Отзыв'
        verbose_name_plural = u'Отзывы'
