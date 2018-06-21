# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import (authenticate, get_user_model)

User = get_user_model()


# ALTERNATIVE REGISTER FORM
class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label=u'Логин', help_text=u'Используйте в этом поле английские буквы')
    email = forms.EmailField(required=True)
    last_name = forms.CharField(label=u'Фамилия', required=True)
    first_name = forms.CharField(label=u'Имя', required=True)

    telephone_1 = forms.RegexField(label=u'Телефон 1', regex=r'^\+?1?\d{9,15}$', help_text=u'Например: +79999999999',
                                   error_message=(u"Формат номера телефона: '+79999999999'. Разрешено до 15 символов."),
                                   required=True)
    telephone_2 = forms.RegexField(label=u'Телефон 2', regex=r'^\+?1?\d{9,15}$',
                                   error_message=(u"Формат номера телефона: '+79999999999'. Разрешено до 15 символов."),
                                   required=False)
    telephone_3 = forms.RegexField(label=u'Телефон 3', regex=r'^\+?1?\d{9,15}$',
                                   error_message=(u"Формат номера телефона: '+79999999999'. Разрешено до 15 символов."),
                                   required=False)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'last_name',  # required
            'first_name',  # required
            'patronymic',
            'country',  # required
            'region',
            'city',
            'adress',
            'index',
            'telephone_1',  # required
            'telephone_2',
            'telephone_3',
            'skype',
            'torgpred_request',
        ]

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        torgpred_request = self.cleaned_data.get('torgpred_request')
        user.save()
        if torgpred_request:
            from cart.views import push_mail
            push_mail(self.cleaned_data, u'Заявка на торгового представителя', ['lse1983@mail.ru', 'feniks-kbr@yandex.ru'],
                      'mail/mail_torgpred.html', False)
        return user


# CUSTOM LOGIN FORM
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError(u'Такого пользователя не существует.')
            if not user.check_password(password):
                raise forms.ValidationError(u'Неправильный пароль.')
            if not user.is_active:
                raise forms.ValidationError(u'Данный пользователь заблокирован.')
        return super(UserLoginForm, self).clean(*args, **kwargs)
