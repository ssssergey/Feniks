# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-08 01:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=255, unique=True, verbose_name='\u0412\u043e\u043f\u0440\u043e\u0441')),
                ('answer', models.TextField(blank=True, unique=True, verbose_name='\u041e\u0442\u0432\u0435\u0442')),
            ],
            options={
                'verbose_name': '\u0412\u043e\u043f\u0440\u043e\u0441\u044b \u0438 \u043e\u0442\u0432\u0435\u0442\u044b',
                'verbose_name_plural': '\u0412\u043e\u043f\u0440\u043e\u0441\u044b \u0438 \u043e\u0442\u0432\u0435\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d')),
                ('rating', models.PositiveSmallIntegerField(choices=[(5, 5), (4, 4), (3, 3), (2, 2), (1, 1)], default=5, verbose_name='\u0420\u0435\u0439\u0442\u0438\u043d\u0433')),
                ('is_approved', models.BooleanField(default=True, verbose_name='\u041e\u0434\u043e\u0431\u0440\u0435\u043d')),
                ('content', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Product', verbose_name='\u0422\u043e\u0432\u0430\u0440')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c')),
            ],
            options={
                'verbose_name': '\u041e\u0442\u0437\u044b\u0432',
                'verbose_name_plural': '\u041e\u0442\u0437\u044b\u0432\u044b',
            },
        ),
        migrations.CreateModel(
            name='SearchTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q', models.CharField(max_length=50, verbose_name='\u041f\u043e\u0438\u0441\u043a\u043e\u0432\u0430\u044f \u0444\u0440\u0430\u0437\u0430')),
                ('search_date', models.DateTimeField(auto_now_add=True, verbose_name='\u041a\u043e\u0433\u0434\u0430 \u0438\u0441\u043a\u0430\u043b\u0438')),
                ('ip_address', models.GenericIPAddressField(verbose_name='IP-\u0430\u0434\u0440\u0435\u0441')),
                ('tracking_id', models.CharField(default='', max_length=50)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c')),
            ],
            options={
                'ordering': ['-search_date'],
                'verbose_name': '\u041f\u043e\u0438\u0441\u043a\u043e\u0432\u044b\u0439 \u0437\u0430\u043f\u0440\u043e\u0441',
                'verbose_name_plural': '\u041f\u043e\u0438\u0441\u043a\u043e\u0432\u044b\u0435 \u0437\u0430\u043f\u0440\u043e\u0441\u044b',
            },
        ),
    ]
