# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, AbstractUser

class UserProfile(AbstractUser):
    # user = models.ForeignKey(User, unique=True)
    patronymic = models.CharField(u'Отчество', max_length=50, blank=True, null=True)
    city = models.CharField(u'Город', max_length=50, blank=True, null=True)
    region = models.CharField(u'Край, область, республика', max_length=50, blank=True, null=True)
    country = models.CharField(u'Страна', max_length=50, default=u'Россия', null=True)
    telephone_1 = models.IntegerField(u'Телефон 1', blank=True, null=True)
    telephone_2 = models.IntegerField(u'Телефон 2', blank=True, null=True)
    telephone_3 = models.IntegerField(u'Телефон 3', blank=True, null=True)
    skype = models.CharField(u'Скайп', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'

    def __unicode__(self):
        return u'Профиль: ' + self.get_full_name()
