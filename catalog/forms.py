# -*- coding: utf-8 -*-
from django import forms
from catalog.models import Product

# class ProductAdminForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = '__all__'
#
#     def clean_price(self):
#         if self.cleaned_data['price'] <= 0:
#             raise forms.ValidationError(u'Цена должна быть положительным числом.')
#         return self.cleaned_data['price']


class ProductAddToCartForm(forms.Form):
    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={'size': '2', 'value': '1', 'class': 'quantity form-control', 'maxlength': '5'}),
        error_messages={'invalid': u'Введите число.'}, min_value=1, label=u'Количество')
    product_slug = forms.CharField(widget=forms.HiddenInput())
    # override the default __init__ so we can set the request
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super(ProductAddToCartForm, self).__init__(*args, **kwargs)

    # custom validation to check for cookies
    def clean(self):
        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError(u"Включите куки в настройках браузера.")
        return self.cleaned_data
