# -*- coding: utf-8 -*-

from django import forms


class ContactForm(forms.Form):
    last_name = forms.CharField(label=u'Фамилия')
    first_name = forms.CharField(label=u'Имя')
    patronymic = forms.CharField(label=u'Отчество', required=False)
    country = forms.CharField(label=u'Страна', initial=u'Российская Федерация')
    region = forms.CharField(label=u'Край, область, республика')
    city = forms.CharField(label=u'Город, село')
    adress = forms.CharField(label=u'Улица и дом')
    index = forms.CharField(label=u'Почтовый индекс', required=False)
    telephone_1 = forms.RegexField(regex=r'^\+?1?\d{9,15}$',label=u"Ваш номер телефона", required=True, help_text=u'например, +79289999999')
    email = forms.EmailField(required=False, label=u"Ваш Email", required=False)
    skype = forms.CharField(label=u'Скайп', required=False)
    DELIVERY = (
        (u'Самовывоз', u'Самовывоз'),
        (u'ПЭК', u'ПЭК'),
        (u'Деловые линии', u'Деловые линии'),
        (u'Байкал сервис', u'Байкал сервис'),
        (u'Кит', u'Кит'),
        (u'Другой', u'Другой'),
    )
    delivery = forms.ChoiceField(label=u'Доставка', choices=DELIVERY)
    PAYMENT = (
        (u'Наличные', u'Наличные'),
        (u'Банковский перевод', u'Банковский перевод'),
        (u'Банковская карта', u'Банковская карта'),
        (u'Другой', u'Другой'),
    )
    payment = forms.ChoiceField(label=u'Оплата', choices=PAYMENT)