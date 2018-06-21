# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    # user = models.ForeignKey(User, unique=True)
    patronymic = models.CharField(u'Отчество', max_length=250, blank=True, null=True)
    country = models.CharField(u'Страна', max_length=250, default=u'Российская Федерация', null=True)
    region = models.CharField(u'Край, область, республика', max_length=250, blank=True, null=True)
    city = models.CharField(u'Населенный пункт', max_length=250, null=True,
                            help_text=u'Например: г. Прохладный или с. Московское')
    adress = models.CharField(u'Улица, дом', max_length=250, blank=True, null=True,
                              help_text=u'Например: ул. Ленина 10 или пер. Красный 5')
    index = models.CharField(u'Почтовый индекс', max_length=250, blank=True, null=True)
    telephone_1 = models.CharField(u'Телефон 1', max_length=250, blank=True, null=True)
    telephone_2 = models.CharField(u'Телефон 2', max_length=250, blank=True, null=True)
    telephone_3 = models.CharField(u'Телефон 3', max_length=250, blank=True, null=True)
    skype = models.CharField(u'Скайп', max_length=250, blank=True, null=True)
    torgpred_request = models.BooleanField(u'Заявка на ТП', default=False,
                                           help_text=u'Я хочу быть вашим торговым представителем (ТП)')

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'

    def __unicode__(self):
        return self.username
