# -*- coding: utf-8 -*-

from django import forms


class ContactForm(forms.Form):
    phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$',label=u"Ваш номер (например, 89289999999)", required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False, label=u"Ваш Email", widget=forms.TextInput(attrs={'class': 'form-control'}))

