# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import UserProfile
from django.contrib.auth.admin import UserAdmin


@admin.register(UserProfile)
class UserAdmin(UserAdmin):
    list_display = ('username', 'last_name', 'first_name', 'city', 'region',)
    list_filter = ('torgpred_request', 'groups', 'city', 'region',)
    list_per_page = 20
    ordering = ['last_name']
    fieldsets = (
        (None, {'fields': ('password',)}),
        (u'Личные данные', {'fields': ('username', 'last_name', 'first_name', 'patronymic')}),
        (u'Местоположение', {'fields': ('city', 'region', 'country',)}),
        (u'Контакты', {'fields': ('email', 'skype', 'telephone_1', 'telephone_2', 'telephone_3')}),
        (u'Разрешения', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (u'Даты', {'fields': ('last_login', 'date_joined')}),
    )
