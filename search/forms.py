# -*- coding: utf-8 -*-

from models import SearchTerm, ProductReview
from django import forms


class SearchForm(forms.ModelForm):
    class Meta:
        model = SearchTerm
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        default_text = u'Поиск'
        self.fields['q'].widget.attrs['value'] = default_text
        self.fields['q'].widget.attrs['class'] = 'form-control'
        self.fields['q'].widget.attrs['onfocus'] = "if (this.value=='" + default_text + "')this.value = ''"

    include = ('q',)


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        exclude = ('user', 'product', 'is_approved')

    def __init__(self, *args, **kwargs):
        super(ProductReviewForm, self).__init__(*args, **kwargs)
        default_text = u'Ваш отзыв'
        self.fields['content'].widget.attrs['value'] = default_text
        self.fields['content'].widget.attrs['class'] = 'form-control'
        self.fields['rating'].widget.attrs['class'] = 'form-control'
        self.fields['rating'].widget.attrs['cols'] = 5
