from django import template
from cart import cart
# from catalog.models import Category
from django.contrib.flatpages.models import FlatPage
from django.db.models import Q
register = template.Library()
import category_tree


@register.inclusion_tag("tags/cart_box.html")
def cart_box(request):
    cart_item_count = cart.cart_distinct_item_count(request)
    return {'cart_item_count': cart_item_count}


@register.inclusion_tag("tags/category_list.html")
def category_list(request_path):
    return {
        'main_tree': category_tree.main_tree,
        'carcass_furniture': category_tree.carcass_furniture,
        'cases': category_tree.cases,
        'beds': category_tree.beds,
        'cushioned_furniture': category_tree.cushioned_furniture,
        'cushioned_furniture_komplekts': category_tree.cushioned_furniture_komplekts,
        'cushioned_furniture_corners': category_tree.cushioned_furniture_corners,
        'cushioned_furniture_sofas': category_tree.cushioned_furniture_sofas,
        'cushioned_furniture_armchairs': category_tree.cushioned_furniture_armchairs,
        'office_furniture': category_tree.office_furniture,
        'fireplaces': category_tree.fireplaces,
        'tables': category_tree.tables,
        'chairs': category_tree.chairs,
        'matrasses': category_tree.matrasses,
        'garden_furniture': category_tree.garden_furniture,
        'kitchen_corners': category_tree.kitchen_corners,
        'bars_restaurants': category_tree.bars_restaurants,
        'interier': category_tree.interier,
        'carcass_furniture_level2': category_tree.carcass_furniture_level2,
        'associated_goods': category_tree.associated_goods,
        'request_path': request_path
    }

@register.inclusion_tag("tags/footer.html")
def footer_links():
    flatpage_list = FlatPage.objects.all()
    return {'flatpage_list': flatpage_list}


@register.inclusion_tag("tags/product_list.html")
def product_list(products, header_text):
    return {'products': products, 'header_text': header_text}
