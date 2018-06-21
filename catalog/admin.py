# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from catalog.models import Product, Material, Architecture


class ProductAdmin(admin.ModelAdmin):
    list_display = ('admin_image', 'name', 'price', 'created_at', 'updated_at',)
    list_filter = ('module_komplekt', 'komplekt_mebel', 'room', 'module_mebel', 'material')
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    readonly_fields = ('admin_image',)
    # sets up slug to be generated from product name
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {'fields': ('sku', 'module_komplekt', 'komplekt_mebel', 'room', 'style', 'material',)}),
        (u'Если это КОМПЛЕКТ', {'fields': ('soft_komplekt',)}),
        (u'Если это МОДУЛЬ', {
            'fields': (
                'peace_of', 'module_mebel', 'module_other', 'doors', 'length', 'architecture_type', 'armchaire_role', 'shape',
                'ochag')
        }),
        (u'Общие', {'fields': (
            'name', 'slug', 'brand', 'country', 'description', 'image', 'image2', 'image3', 'image4', 'image5', 'price',
            'price_bulk1',
            'garantee', 'on_order', 'is_active', 'is_bestseller', 'is_featured'
        )}),
        (u'Служебные', {
            'fields': ('meta_keywords', 'meta_description',)
        }),
    )
    change_list_template = 'admin_custom/change_list_custom.html'


admin.site.register(Product, ProductAdmin)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Material, MaterialAdmin)


class ArchitectureAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Architecture, ArchitectureAdmin)
