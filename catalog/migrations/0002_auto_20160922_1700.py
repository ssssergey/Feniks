# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-22 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='peace_of',
        ),
        migrations.AddField(
            model_name='product',
            name='peace_of',
            field=models.ManyToManyField(blank=True, null=True, related_name='_product_peace_of_+', to='catalog.Product', verbose_name='\u041e\u0442\u043d\u043e\u0441\u0438\u0442\u0441\u044f \u043a \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0442\u0443'),
        ),
    ]
