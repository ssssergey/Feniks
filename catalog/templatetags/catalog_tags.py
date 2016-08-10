# -*- coding: utf-8 -*-
from django import template
from cart import cart
from django.core.urlresolvers import reverse
# from catalog.models import Category
# from django.contrib.flatpages.models import FlatPage
from django.db.models import Q

register = template.Library()
import category_tree


@register.inclusion_tag("tags/cart_box.html")
def cart_box(request):
    cart_item_count = cart.cart_distinct_item_count(request)
    return {'cart_item_count': cart_item_count}


@register.inclusion_tag("tags/category_list.html")
def category_list(request_path):
    # categories = {
    #     'main_tree': category_tree.main_tree,
    #     'carcass_furniture': category_tree.carcass_furniture,
    #     'carcass_furniture_level2': category_tree.carcass_furniture_level2,
    #     'associated_goods': category_tree.associated_goods,
    #     'cases': category_tree.cases,
    #     'beds': category_tree.beds,
    #     'cushioned_furniture': category_tree.cushioned_furniture,
    #     'cushioned_furniture_komplekts': category_tree.cushioned_furniture_komplekts,
    #     'cushioned_furniture_corners': category_tree.cushioned_furniture_corners,
    #     'cushioned_furniture_sofas': category_tree.cushioned_furniture_sofas,
    #     'cushioned_furniture_armchairs': category_tree.cushioned_furniture_armchairs,
    #     'office_furniture': category_tree.office_furniture,
    #     'fireplaces': category_tree.fireplaces,
    #     'kamin_komplekti': category_tree.kamin_komplekti,
    #     'serii': category_tree.serii,
    #     'portals': category_tree.portals,
    #     'electrokamins': category_tree.electrokamins,
    #     'tables': category_tree.tables,
    #     'tables_level2': category_tree.tables_level2,
    #     'tables_level3': category_tree.tables_level3,
    #     'tables_others': category_tree.tables_others,
    #     'chairs': category_tree.chairs,
    #     'chairs_others': category_tree.chairs_others,
    #     'matrasses': category_tree.matrasses,
    #     'rotang': category_tree.rotang,
    #     'garden_furniture': category_tree.garden_furniture,
    #     'rotang_level2': category_tree.rotang_level2,
    #     'rotang_level3': category_tree.rotang_level3,
    #     'kitchen_corners': category_tree.kitchen_corners,
    #     'kitchen_corners_level2': category_tree.kitchen_corners_level2,
    #     'kitchen_corners_level3': category_tree.kitchen_corners_level3,
    #     'bars_restaurants': category_tree.bars_restaurants,
    #     'interier': category_tree.interier,
    #     'vases': category_tree.vases,
    #     'request_path': request_path
    # }

    cats = [
        {
            'title': u'Корпусная мебель',
            'link': reverse('carcass_furniture_base'),
        },
        {
            'title': u'Мягкая мебель',
            'link': reverse('cushioned_furniture_base'),
        },
        {
            'title': u'Офисная мебель',
            'link': reverse('office_furniture_base'),
        },
        {
            'title': u'Камины',
            'link': reverse('fireplace_base'),
        },
        {
            'title': u'Столы',
            'link': reverse('tables_base'),
        },
        {
            'title': u'Стулья',
            'link': reverse('chairs_base'),
        },
        {
            'title': u'Кухонные уголки',
            'link': reverse('kitchen_corners_base'),
        },
        {
            'title': u'Матрасы',
            'link': reverse('matrasses_base'),
        },
        {
            'title': u'Садовая мебель',
            'link': reverse('garden_furniture_base'),
        },
        {
            'title': u'Для баров и ресторанов',
            'link': reverse('bars_restaurants_base'),
        },
        {
            'title': u'Шкафы-купе',
            'link': reverse('case_kupe'),
        },
        {
            'title': u'Гостиничные номера',
            'link': reverse('hotels'),
        },
        {
            'title': u'Интерьер',
            'link': reverse('interier_base'),
        },
        {
            'title': u'Разное',
            'link': reverse('others'),
        },
        {
            'title': u'Сопутствующие товары',
            'link': reverse('associated_goods_base'),
        },
        {
            'title': u'Индивидуальные заказы',
            'link': reverse('individual_orders'),
        },
    ]
    return {'cats': cats,
            'request_path': request_path
            }


@register.inclusion_tag("tags/footer.html")
def footer_links():
    # flatpage_list = FlatPage.objects.all()
    return {
        # 'flatpage_list': flatpage_list
    }


@register.inclusion_tag("tags/product_list.html")
def product_list(products, header_text):
    return {'products': products, 'header_text': header_text}
