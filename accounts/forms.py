# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import (authenticate, login, logout, get_user_model)
from django.contrib.auth.models import Group

User = get_user_model()

# REGISTER FORM
class RegisterForm(UserCreationForm):
    torg_pred = forms.BooleanField(label=u'Я хочу быть торговым представителем')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = u'Используйте английские буквы'

# widget_torgpred=forms.TextInput(attrs={'placeholder': u'Обязательно для ТП'})

# ALTERNATIVE REGISTER FORM
class UserRegisterForm(forms.ModelForm):
    torgpred = forms.BooleanField(label=u'Я хочу быть торговым представителем (ТП)', required=False)
    username = forms.CharField(label=u'Короткое имя пользователя (логин)', help_text=u'Используйте в этом поле английские буквы')
    email = forms.EmailField(required=True)
    # password = forms.CharField(widget=forms.PasswordInput)
    # last_name = forms.CharField(label=u'Фамилия', required = True)
    # first_name = forms.CharField(label=u'Имя', required = True)

    telephone_1 = forms.RegexField(label=u'Телефон 1', regex=r'^\+?1?\d{9,15}$', help_text=u'Например: +79999999999',
                                   error_message=(u"Формат номера телефона: '+79999999999'. Разрешено до 15 символов."), required=True)
    telephone_2 = forms.RegexField(label=u'Телефон 2', regex=r'^\+?1?\d{9,15}$',
                                   error_message=(u"Формат номера телефона: '+79999999999'. Разрешено до 15 символов."), required=False)
    telephone_3 = forms.RegexField(label=u'Телефон 3', regex=r'^\+?1?\d{9,15}$',
                                   error_message=(u"Формат номера телефона: '+79999999999'. Разрешено до 15 символов."), required=False)


    class Meta:
        model = User
        # exclude = ['last_login', 'groups', 'is_superuser', 'user_permissions']
        fields = [
            'username',
            'email',
            'password',
            'last_name',    # required
            'first_name',   # required
            'patronymic',
            'country',      # required
            'region',
            'city',
            'adress',
            'index',
            'telephone_1',  # required
            'telephone_2',
            'telephone_3',
            'skype',
        ]

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        torgpred = self.cleaned_data.get('torgpred')
        user.save()
        if torgpred:
            group, created = Group.objects.get_or_create(name=u'Торговые представители')
            user.groups.add(group)
        return user


# group = Group.objects.get(name='groupname')
# user.groups.add(group)

    # def clean_torgpred(self):
    #     torgpred = self.cleaned_data.get('torgpred')
    #     if torgpred:
    #         if





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
