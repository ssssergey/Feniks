# -*- coding: utf-8 -*-
from django import template
from django.core.urlresolvers import reverse

from cart import cart

register = template.Library()


@register.inclusion_tag("tags/cart_box.html")
def cart_box(request):
    cart_item_count = cart.cart_distinct_item_count(request)
    return {'cart_item_count': cart_item_count}


@register.inclusion_tag("tags/category_list.html")
def category_list(request_path):
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
            'title': u'Обеденные группы',
            'link': reverse('dinner_groups'),
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
