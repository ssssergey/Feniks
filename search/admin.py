# -*- coding: utf-8 -*-
from django.contrib import admin
from models import SearchTerm, Faq
from .models import ProductReview


class SearchTermAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'ip_address', 'search_date')
    list_filter = ('ip_address', 'user', 'q')
    exclude = ('user',)


admin.site.register(SearchTerm, SearchTermAdmin)


class FaqAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'question', 'answer')


admin.site.register(Faq, FaqAdmin)


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'date', 'rating', 'is_approved')
    list_per_page = 20
    list_filter = ('product', 'user', 'is_approved')
    ordering = ['date']
    search_fields = ['user', 'content']


admin.site.register(ProductReview, ProductReviewAdmin)
