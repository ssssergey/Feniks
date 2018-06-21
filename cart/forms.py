# -*- coding: utf-8 -*-

from django import forms
from .models import Order
import re


def strip_non_numbers(data):
    """ gets rid of all non-number characters """
    non_numbers = re.compile('\D')
    return non_numbers.sub('', data)


class CheckoutForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CheckoutForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Order
        exclude = ('status', 'ip_address', 'user', 'last_updated')

    def clean_phone(self):
        phone = self.cleaned_data['telephone_1']
        stripped_phone = strip_non_numbers(phone)
        if len(stripped_phone) < 10:
            raise forms.ValidationError(u"Формат номера телефона: '+79999999999'. Разрешено до 15 символов.")
        return self.cleaned_data['phone']


class PriceForm(forms.Form):
    price = forms.IntegerField()
