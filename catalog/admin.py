# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from catalog.models import Product, ProductReview
from accounts.models import UserProfile


@admin.register(UserProfile)
class UserAdmin(UserAdmin):
    list_display = ('username', 'last_name', 'first_name', 'city', 'region',)
    list_filter = ('groups', 'city', 'region',)
    list_per_page = 20
    ordering = ['last_name']
    fieldsets = (
        (None, {'fields': ('password',)}),
        (u'Личные данные', {'fields': ('username', 'last_name', 'first_name', 'patronymic')}),
        (u'Местоположение', {'fields': ('city', 'region', 'country',)}),
        (u'Контакты', {'fields': ('email', 'skype', 'telephone_1', 'telephone_2', 'telephone_3')}),
        (u'Разрешения', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions')}),
        (u'Даты', {'fields': ('last_login', 'date_joined')}),
    )


class ProductAdmin(admin.ModelAdmin):
    # form = ProductAdminForm
    # sets values for how the admin site lists your products
    list_display = ('admin_image', 'name', 'price', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    readonly_fields = ('admin_image',)
    # exclude = ('created_at', 'updated_at',)
    # sets up slug to be generated from product name
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {'fields': ('module_komplekt', 'room', 'style', 'material', 'admin_image',)}),
        (u'Для комплектов', {'fields': ('komplekt_mebel', 'soft_komplekt',)}),
        (u'Для модулей', {
            'fields': (
            'peace_of', 'module_mebel', 'module_other', 'doors', 'length', 'architecture_type', 'armchaire_role', 'shape',
            'ochag')
        }),
        (u'Общие', {'fields': (
            'name', 'slug', 'brand', 'country', 'description', 'image', 'image2', 'image3', 'price', 'price_bulk1', 'price_bulk2',
            'price_bulk3',
            'quantity', 'garantee', 'on_order', 'is_active', 'is_bestseller', 'is_featured'
        )}),
        (u'Служебные', {
            'fields': ('meta_keywords', 'meta_description',)
        }),
    )

# registers your product model with the admin site
admin.site.register(Product, ProductAdmin)

# class CategoryAdmin(admin.ModelAdmin):
#     #sets up values for how admin site lists categories
#     list_display = ('name', 'created_at', 'updated_at',)
#     list_display_links = ('name',)
#     list_per_page = 20
#     ordering = ['name']
#     search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
#     exclude = ('created_at', 'updated_at',)
#     # sets up slug to be generated from category name
#     prepopulated_fields = {'slug' : ('name',)}
# admin.site.register(Category, CategoryAdmin)

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'date', 'rating', 'is_approved')
    list_per_page = 20
    list_filter = ('product', 'user', 'is_approved')
    ordering = ['date']
    search_fields = ['user', 'content']


admin.site.register(ProductReview, ProductReviewAdmin)
