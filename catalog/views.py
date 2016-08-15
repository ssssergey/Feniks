# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render_to_response, render
from catalog.models import Product
from search.models import ProductReview
from django.template import RequestContext
from django.db.models import Q
from django.core import urlresolvers
from cart import cart
from django.http import HttpResponseRedirect
from forms import ProductAddToCartForm
from search.forms import ProductReviewForm

from stats import stats
from Feniks.settings import PRODUCTS_PER_ROW
from django.core.urlresolvers import reverse


def index(request, template_name="catalog/index.html"):
    page_title = u'Феникс'
    new_products = Product.active.all()
    new_products = [i for i in new_products if i.new()][0:PRODUCTS_PER_ROW]
    search_recs = stats.recommended_from_search(request)
    featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
    recently_viewed = stats.get_recently_viewed(request)
    view_recs = stats.recommended_from_views(request)
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def about(request, template_name="flatpages/about.html"):
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def contact(request, template_name="flatpages/contact.html"):
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


from cart.models import Delivery


def delivery(request, template_name="flatpages/delivery.html"):
    deliveries = Delivery.objects.all()
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


from search.models import Faq


def faq(request, template_name="flatpages/faq.html"):
    faqs = Faq.objects.all()
    return render(request, template_name, {'faqs': faqs})


#################### Catalog list ###############################

################### carcass furniture #########################

def carcass_furniture_base(request, template_name="catalog/category.html"):
    category_name = u'Корпусная мебель'
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель'))
    subcategories = (
        (u'Кухни', reverse('carcass_furniture_kitchens_base')),
        (u'Горки, стенки, гостинные', reverse('carcass_furniture_gorki_stenki_gestrooms_base')),
        (u'Спальни', reverse('carcass_furniture_bedrooms_base')),
        (u'Прихожие', reverse('carcass_furniture_corridors_base')),
        (u'Детские', reverse('carcass_furniture_children_rooms_base')),
        (u'Шкафы', reverse('carcass_furniture_cases_base')),
        (u'Кровати', reverse('carcass_furniture_beds_base')),
        (u'ТВ-тумбы', reverse('carcass_furniture_tv_tumbs_base')),
        (u'Другая мебель', reverse('carcass_furniture_other_furniture')),
    )
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_kitchens_base(request, template_name="catalog/category.html"):
    category_name = u'Корпусная мебель - Кухни'
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель') & Q(room=u'Кухня'))
    subcategories = (
        (u'Комплекты', reverse('carcass_furniture_kitchens', args=('komplekts',))),
        (u'Модульно', reverse('carcass_furniture_kitchens', args=('modules',))),
        (u'Сопутствующие товары', reverse('associated_goods_base')),
    )
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_kitchens(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель') & Q(room=u'Кухня'))
    if type == 'komplekts':
        products = products.filter(Q(module_komplekt=u'Комплект'))
        category_name = u'Корпусная мебель - Кухни - Комплекты'
    elif type == 'modules':
        products = products.filter(Q(module_komplekt=u'Модуль'))
        category_name = u'Корпусная мебель - Кухни - Модули'
    # elif type == 'others':
    #     products = products.filter(Q(module_komplekt__isnull=True))
    #     category_name = u'Корпусная мебель - Кухни - Другое'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_gorki_stenki_gestrooms_base(request, template_name="catalog/category.html"):
    category_name = u'Корпусная мебель - Горки, стенки, гостинные'
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель') & Q(room=u'Гостиная(горки, стенки)'))
    subcategories = (
        (u'Комплекты', reverse('carcass_furniture_gorki_stenki_gestrooms', args=('komplekts',))),
        (u'Модульно', reverse('carcass_furniture_gorki_stenki_gestrooms', args=('modules',))),
        (u'Другое', reverse('carcass_furniture_gorki_stenki_gestrooms', args=('others',))),
        (u'Библиотека', reverse('carcass_furniture_gorki_stenki_gestrooms', args=('libraries',))),
        (u'Сопутствующие товары', reverse('associated_goods_base')),
    )
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_gorki_stenki_gestrooms(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель') & Q(room=u'Гостиная(горки, стенки)'))
    if type == 'komplekts':
        products = products.filter(Q(module_komplekt=u'Комплект'))
        category_name = u'Корпусная мебель - Горки, стенки, гостинные - Комплекты'
    elif type == 'modules':
        products = products.filter(Q(module_komplekt=u'Модуль'))
        category_name = u'Корпусная мебель - Горки, стенки, гостинные - Модули'
    elif type == 'others':
        products = products.filter(Q(module_komplekt__isnull=True))
        category_name = u'Корпусная мебель - Горки, стенки, гостинные - Другое'
    elif type == 'libraries':
        products = products.filter(Q(module_mebel=u'Библиотека'))
        category_name = u'Корпусная мебель - Горки, стенки, гостинные - Библиотеки'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_bedrooms_base(request, template_name="catalog/category.html"):
    category_name = u'Корпусная мебель - Спальни'
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель') & Q(room=u'Спальня'))
    subcategories = (
        (u'Комплекты', reverse('carcass_furniture_bedrooms', args=('komplekts',))),
        (u'Модульно', reverse('carcass_furniture_bedrooms', args=('modules',))),
        (u'Другое', reverse('carcass_furniture_bedrooms', args=('others',))),
        (u'Сопутствующие товары', reverse('associated_goods_base')),
    )
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_bedrooms(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель') & Q(room=u'Спальня'))
    if type == 'komplekts':
        products = products.filter(Q(module_komplekt=u'Комплект'))
        category_name = u'Корпусная мебель - Спальни - Комплекты'
    elif type == 'modules':
        products = products.filter(Q(module_komplekt=u'Модуль'))
        category_name = u'Корпусная мебель - Спальни - Модули'
    elif type == 'others':
        products = products.filter(Q(module_komplekt__isnull=True))
        category_name = u'Корпусная мебель - Спальни - Другое'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_corridors_base(request, template_name="catalog/category.html"):
    category_name = u'Корпусная мебель - Прихожие'
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель') & Q(room=u'Прихожие'))
    subcategories = (
        (u'Комплекты', reverse('carcass_furniture_corridors', args=('komplekts',))),
        (u'Модульно', reverse('carcass_furniture_corridors', args=('modules',))),
        (u'Другое', reverse('carcass_furniture_corridors', args=('others',))),
        (u'Сопутствующие товары', reverse('associated_goods_base')),
    )
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_corridors(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель') & Q(room=u'Прихожие'))
    if type == 'komplekts':
        products = products.filter(Q(module_komplekt=u'Комплект'))
        category_name = u'Корпусная мебель - Прихожие - Комплекты'
    elif type == 'modules':
        products = products.filter(Q(module_komplekt=u'Модуль'))
        category_name = u'Корпусная мебель - Прихожие - Модули'
    elif type == 'others':
        products = products.filter(Q(module_komplekt__isnull=True))
        category_name = u'Корпусная мебель - Прихожие - Другое'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_children_rooms_base(request, template_name="catalog/category.html"):
    category_name = u'Корпусная мебель - Детские'
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель') & Q(room=u'Детские'))
    subcategories = (
        (u'Комплекты', reverse('carcass_furniture_children_rooms', args=('komplekts',))),
        (u'Модульно', reverse('carcass_furniture_children_rooms', args=('modules',))),
        (u'Другое', reverse('carcass_furniture_children_rooms', args=('others',))),
        (u'Сопутствующие товары', reverse('associated_goods_base')),
    )
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_children_rooms(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель') & Q(room=u'Детские'))
    if type == 'komplekts':
        products = products.filter(Q(module_komplekt=u'Комплект'))
        category_name = u'Корпусная мебель - Детские - Комплект'
    elif type == 'modules':
        products = products.filter(Q(module_komplekt=u'Модуль'))
        category_name = u'Корпусная мебель - Детские - Модули'
    elif type == 'others':
        products = products.filter(Q(module_komplekt__isnull=True))
        category_name = u'Корпусная мебель - Детские - Другое'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_tv_tumbs_base(request, template_name="catalog/category.html"):
    category_name = u'Корпусная мебель - ТВ-тумбы'
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель') & Q(module_mebel=u'ТВ-тумба'))
    subcategories = (
        (u'Комплекты', reverse('carcass_furniture_tv_tumbs', args=('komplekts',))),
        (u'Модульно', reverse('carcass_furniture_tv_tumbs', args=('modules',))),
        (u'Другое', reverse('carcass_furniture_tv_tumbs', args=('others',))),
        (u'Сопутствующие товары', reverse('associated_goods_base')),
    )
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_tv_tumbs(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель') & Q(module_mebel=u'ТВ-тумба'))
    if type == 'komplekts':
        products = products.filter(Q(module_komplekt=u'Комплект'))
        category_name = u'Корпусная мебель - ТВ-тумбы - Комплекты'
    elif type == 'modules':
        products = products.filter(Q(module_komplekt=u'Модуль'))
        category_name = u'Корпусная мебель - ТВ-тумбы - Модули'
    elif type == 'others':
        products = products.filter(Q(module_komplekt__isnull=True))
        category_name = u'Корпусная мебель - ТВ-тумбы - Другие'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_other_furniture(request, template_name="catalog/category.html"):
    category_name = u'Корпусная мебель - Другая мебель'
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель') & Q(room=u'Другое'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_cases_base(request, template_name="catalog/category.html"):
    category_name = u'Корпусная мебель - Шкаф'
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель') & Q(module_mebel=u'Шкаф'))
    subcategories = (
        (u'1-о дверные', reverse('carcass_furniture_cases', args=('doors_1',))),
        (u'2-х дверные', reverse('carcass_furniture_cases', args=('doors_2',))),
        (u'3-х дверные', reverse('carcass_furniture_cases', args=('doors_3',))),
        (u'4-х дверные', reverse('carcass_furniture_cases', args=('doors_4',))),
        (u'5-х дверные', reverse('carcass_furniture_cases', args=('doors_5',))),
        (u'6-х дверные', reverse('carcass_furniture_cases', args=('doors_6',))),
        (u'Угловые', reverse('carcass_furniture_cases', args=('cases_corners',))),
        (u'Другое', reverse('carcass_furniture_cases', args=('cases_others',))),
    )
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_cases(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель'))
    if type == 'doors_1':
        products = products.filter(Q(doors=1))
        category_name = u'Корпусная мебель - Шкафы - 1-о дверные'
    elif type == 'doors_2':
        products = products.filter(Q(doors=2))
        category_name = u'Корпусная мебель - Шкафы - 2-х дверные'
    elif type == 'doors_3':
        products = products.filter(Q(doors=3))
        category_name = u'Корпусная мебель - Шкафы - 3-х дверные'
    elif type == 'doors_4':
        products = products.filter(Q(doors=4))
        category_name = u'Корпусная мебель - Шкафы - 4-х дверные'
    elif type == 'doors_5':
        products = products.filter(Q(doors=5))
        category_name = u'Корпусная мебель - Шкафы - 5-х дверные'
    elif type == 'doors_6':
        products = products.filter(Q(doors=6))
        category_name = u'Корпусная мебель - Шкафы - 6-х дверные'
    elif type == 'cases_corners':
        products = products.filter(Q(shape=u'Угловой'))
        category_name = u'Корпусная мебель - Шкафы - Угловые'
    elif type == 'cases_others':
        products = products.filter(Q(doors__gte=6))
        category_name = u'Корпусная мебель - Шкафы - Другое'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_beds_base(request, template_name="catalog/category.html"):
    category_name = u'Корпусная мебель - Кровати'
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель') & Q(module_mebel=u'Кровать'))
    subcategories = (
        (u'80 см', reverse('carcass_furniture_beds', args=('length_80',))),
        (u'90 см', reverse('carcass_furniture_beds', args=('length_90',))),
        (u'120 см', reverse('carcass_furniture_beds', args=('length_120',))),
        (u'140 см', reverse('carcass_furniture_beds', args=('length_140',))),
        (u'160 см', reverse('carcass_furniture_beds', args=('length_160',))),
        (u'180 см', reverse('carcass_furniture_beds', args=('length_180',))),
        (u'Двухъярусные', reverse('carcass_furniture_beds', args=('double',))),
        (u'Другое', reverse('carcass_furniture_beds', args=('others',))),
    )
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_beds(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель'))
    if type == 'length_80':
        products = products.filter(Q(length=80))
        category_name = u'Корпусная мебель - Кровати - 80 см'
    elif type == 'length_90':
        products = products.filter(Q(length=90))
        category_name = u'Корпусная мебель - Кровати - 90 см'
    elif type == 'length_120':
        products = products.filter(Q(length=120))
        category_name = u'Корпусная мебель - Кровати - 120 см'
    elif type == 'length_140':
        products = products.filter(Q(length=140))
        category_name = u'Корпусная мебель - Кровати - 140 см'
    elif type == 'length_160':
        products = products.filter(Q(length=160))
        category_name = u'Корпусная мебель - Кровати - 160 см'
    elif type == 'length_180':
        products = products.filter(Q(length=180))
        category_name = u'Корпусная мебель - Кровати - 180 см'
    elif type == 'double':
        products = products.filter(Q(architecture_type__name=u'Двухъярусная кровать'))
        category_name = u'Корпусная мебель - Кровати - Двухъярусные'
    elif type == 'others':
        products = products.filter(Q(length__gte=180))
        category_name = u'Корпусная мебель - Кровати - Другое'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


################### Мягкая мебель ########################3

def cushioned_furniture_base(request, template_name="catalog/category.html"):
    category_name = u'Мягкая мебель'
    products = Product.active.filter(Q(komplekt_mebel=u'Мягкая мебель'))
    subcategories = (
        (u'Комплекты', reverse('cushioned_furniture_komplekts_base')),
        (u'Угловые', reverse('cushioned_furniture_corners_base')),
        (u'Диваны', reverse('cushioned_furniture_sofas_base')),
        (u'Кресла', reverse('cushioned_furniture_armchairs_base')),
        (u'Под заказ', reverse('cushioned_furniture_on_orders')),
    )
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def cushioned_furniture_komplekts_base(request, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Мягкая мебель') & Q(module_komplekt=u'Комплект'))
    category_name = u'Мягкая мебель - Комплекты'
    subcategories = (
        (u'Диван + 2 кресла-кровати', reverse('cushioned_furniture_komplekts', args=('d_2kr_kr',))),
        (u'Диван + 2 кресла + кресло-кровать', reverse('cushioned_furniture_komplekts', args=('d_2kr_kr_kr',))),
        (u'Диван-кровать + 2 кресла-кровати', reverse('cushioned_furniture_komplekts', args=('d_kr_2kr_kr',))),
        (u'Глухой диван + 2 глухих кресла', reverse('cushioned_furniture_komplekts', args=('glkr_2glkr',))),
        (u'Угловой диван + глухое кресло', reverse('cushioned_furniture_komplekts', args=('ugd_glkr',))),
        (u'Угловой диван + кресло-кровать', reverse('cushioned_furniture_komplekts', args=('ugd_krkr',))),
    )
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def cushioned_furniture_komplekts(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Мягкая мебель') & Q(module_komplekt=u'Комплект'))
    if type == 'd_2kr_kr':
        products = products.filter(Q(soft_komplekt=u'Диван + 2 кресла-кровати'))
        category_name = u'Мягкая мебель - Комплекты - Диван + 2 кресла-кровати'
    elif type == 'd_2kr_kr_kr':
        products = products.filter(Q(soft_komplekt=u'Диван + 2 кресла + кресло-кровать'))
        category_name = u'Мягкая мебель - Комплекты - Диван + 2 кресла + кресло-кровать'
    elif type == 'd_kr_2kr_kr':
        products = products.filter(Q(soft_komplekt=u'Диван-кровать + 2 кресла-кровати'))
        category_name = u'Мягкая мебель - Комплекты - Диван-кровать + 2 кресла-кровати'
    elif type == 'glkr_2glkr':
        products = products.filter(Q(soft_komplekt=u'Глухой диван + 2 глухих кресла'))
        category_name = u'Мягкая мебель - Комплекты - Глухой диван + 2 глухих кресла'
    elif type == 'ugd_glkr':
        products = products.filter(Q(soft_komplekt=u'Угловой диван + глухое кресло'))
        category_name = u'Мягкая мебель - Комплекты - Угловой диван + глухое кресло'
    elif type == 'ugd_krkr':
        products = products.filter(Q(soft_komplekt=u'Угловой диван + кресло-кровать'))
        category_name = u'Мягкая мебель - Комплекты - Угловой диван + кресло-кровать'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def cushioned_furniture_corners_base(request, template_name="catalog/category.html"):
    category_name = u'Мягкая мебель - Угловые'
    products = Product.active.filter(Q(komplekt_mebel=u'Мягкая мебель') & Q(shape=u'Угловые'))
    subcategories = (
        (u'Выкатные', reverse('cushioned_furniture_corners', args=('rollable',))),
        (u'Классические', reverse('cushioned_furniture_corners', args=('classic',))),
        (u'Металлокаркас', reverse('cushioned_furniture_corners', args=('metalkarkas',))),
        (u'Евро', reverse('cushioned_furniture_corners', args=('euro',))),
    )
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def cushioned_furniture_corners(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Мягкая мебель') & Q(shape=u'Угловые'))
    if type == 'rollable':
        products = products.filter(Q(architecture_type__name=u'Выкатные'))
        category_name = u'Мягкая мебель - Угловые - Выкатные'
    elif type == 'classic':
        products = products.filter(Q(architecture_type__name=u'Классические'))
        category_name = u'Мягкая мебель - Угловые - Классические'
    elif type == 'metalkarkas':
        products = products.filter(Q(material__name=u'Металлокаркас'))
        category_name = u'Мягкая мебель - Угловые - Металлокаркас'
    elif type == 'euro':
        products = products.filter(Q(architecture_type__name=u'Евро'))
        category_name = u'Мягкая мебель - Угловые - Евро'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def cushioned_furniture_sofas_base(request, template_name="catalog/category.html"):
    category_name = u'Мягкая мебель - Диваны'
    products = Product.active.filter(Q(komplekt_mebel=u'Мягкая мебель') & Q(module_mebel=u'Диван'))
    subcategories = (
        (u'Классические', reverse('cushioned_furniture_sofas', args=('classic',))),
        (u'Евро-книжка', reverse('cushioned_furniture_sofas', args=('euro_book',))),
        (u'Книжка', reverse('cushioned_furniture_sofas', args=('book',))),
        (u'Выкатные', reverse('cushioned_furniture_sofas', args=('rollable',))),
        (u'Металлокаркас', reverse('cushioned_furniture_sofas', args=('metalkarkas',))),
        (u'Мини', reverse('cushioned_furniture_sofas', args=('mini',))),
        (u'Офисные', reverse('cushioned_furniture_sofas', args=('office',))),
        (u'Ротанг', reverse('cushioned_furniture_sofas', args=('rotang',))),
    )
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def cushioned_furniture_sofas(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Мягкая мебель') & Q(module_mebel=u'Диван'))
    if type == 'classic':
        products = products.filter(Q(architecture_type__name=u'Классические'))
        category_name = u'Мягкая мебель - Диваны - Классические'
    elif type == 'euro_book':
        products = products.filter(Q(architecture_type__name=u'Евро-книжка'))
        category_name = u'Мягкая мебель - Диваны - Евро-книжка'
    elif type == 'book':
        products = products.filter(Q(architecture_type__name=u'Книжка'))
        category_name = u'Мягкая мебель - Диваны - Книжка'
    elif type == 'rollable':
        products = products.filter(Q(architecture_type__name=u'Выкатные'))
        category_name = u'Мягкая мебель - Диваны - Выкатные'
    elif type == 'metalkarkas':
        products = products.filter(Q(architecture_type__name=u'Металлокаркас') | Q(material__name=u'Металлокаркас'))
        category_name = u'Мягкая мебель - Диваны - Металлокаркас'
    elif type == 'mini':
        products = products.filter(Q(architecture_type__name=u'Мини'))
        category_name = u'Мягкая мебель - Диваны - Мини'
    elif type == 'office':
        products = products.filter(Q(architecture_type__name=u'Офисные') | Q(style=u'Офисные'))
        category_name = u'Мягкая мебель - Диваны - Офисные'
    elif type == 'rotang':
        products = products.filter(Q(material__name__icontains=u'Ротанг'))
        category_name = u'Мягкая мебель - Диваны - Ротанг'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def cushioned_furniture_armchairs_base(request, template_name="catalog/category.html"):
    category_name = u'Мягкая мебель - Кресла'
    products = Product.active.filter(Q(komplekt_mebel=u'Мягкая мебель') & Q(module_mebel=u'Кресло'))
    subcategories = (
        (u'Классические', reverse('cushioned_furniture_armchairs', args=('classic',))),
        (u'Кресла-кровати', reverse('cushioned_furniture_armchairs', args=('armchair_bed',))),
        (u'Кресла-качалки', reverse('cushioned_furniture_armchairs', args=('armchair_kachalka',))),
        (u'Офисные', reverse('cushioned_furniture_armchairs', args=('office_chair',))),
        (u'Банкетка', reverse('cushioned_furniture_armchairs', args=('banketka',))),
    )
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def cushioned_furniture_armchairs(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Мягкая мебель') & Q(module_mebel=u'Кресло'))
    if type == 'classic':
        products = products.filter(Q(architecture_type__name=u'Классические'))
        category_name = u'Мягкая мебель - Кресла - Классические'
    elif type == 'armchair_bed':
        products = products.filter(Q(architecture_type__name=u'Кресла-кровати'))
        category_name = u'Мягкая мебель - Кресла - Кресла-кровати'
    elif type == 'armchair_kachalka':
        products = products.filter(Q(architecture_type__name=u'Кресла-качалки'))
        category_name = u'Мягкая мебель - Кресла - Кресла-качалки'
    elif type == 'office_chair':
        products = products.filter(Q(architecture_type__name=u'Офисные') | Q(style=u'Офисные'))
        category_name = u'Мягкая мебель - Кресла - Офисные'
    elif type == 'banketka':
        products = products.filter(Q(architecture_type__name=u'Банкетка'))
        category_name = u'Мягкая мебель - Кресла - Банкетка'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def cushioned_furniture_on_orders(request, template_name="catalog/category.html"):
    category_name = u'Мягкая мебель - Под заказ'
    products = Product.active.filter(Q(komplekt_mebel=u'Мягкая мебель') & Q(on_order=True))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


######################### Офисная мебель ############################

def office_furniture_base(request, template_name="catalog/category.html"):
    category_name = u'Офисная мебель'
    subcategories = (
        (u'Диваны', reverse('office_furniture_sofas_base')),
        (u'Столы', reverse('office_furniture_tables')),
        (u'Шкафы', reverse('office_furniture_cases')),
        (u'Библиотеки', reverse('office_furniture_libraries')),
        (u'Кресла', reverse('office_furniture_armchairs_base')),
        (u'Стулья', reverse('office_furniture_chairs_base')),
        (u'Перегородки', reverse('office_furniture_divider_base')),
    )
    products = Product.active.filter(Q(komplekt_mebel=u'Офисная мебель'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def office_furniture_sofas_base(request, template_name="catalog/category.html"):
    category_name = u'Офисная мебель - Диваны'
    products = Product.active.filter(Q(komplekt_mebel=u'Офисная мебель') & Q(module_mebel=u'Диван'))
    subcategories = (
        (u'Прямые', reverse('office_furniture_sofas', args=('strait',))),
        (u'Угловые', reverse('office_furniture_sofas', args=('corner',))),
    )
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def office_furniture_sofas(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Офисная мебель') & Q(module_mebel=u'Диван'))
    if type == 'strait':
        products = products.filter(Q(shape=u'Прямые'))
        category_name = u'Офисная мебель - Диваны - Прямые'
    elif type == 'corner':
        products = products.filter(Q(shape=u'Угловые'))
        category_name = u'Офисная мебель - Диваны - Угловые'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def office_furniture_tables(request, template_name="catalog/category.html"):
    category_name = u'Офисная мебель - Столы'
    products = Product.active.filter(Q(komplekt_mebel=u'Офисная мебель') & Q(module_mebel=u'Стол'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def office_furniture_cases(request, template_name="catalog/category.html"):
    category_name = u'Офисная мебель - Шкафы'
    products = Product.active.filter(Q(komplekt_mebel=u'Офисная мебель') & Q(module_mebel=u'Шкаф'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def office_furniture_libraries(request, template_name="catalog/category.html"):
    category_name = u'Офисная мебель - Библиотеки'
    products = Product.active.filter(Q(komplekt_mebel=u'Офисная мебель') & Q(module_mebel=u'Библиотека'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def office_furniture_armchairs_base(request, template_name="catalog/category.html"):
    category_name = u'Офисная мебель - Кресла'
    products = Product.active.filter(Q(komplekt_mebel=u'Офисная мебель') & Q(module_mebel=u'Кресло'))
    subcategories = (
        (u'Для руководителя', reverse('office_furniture_armchairs', args=('chief',))),
        (u'Для персонала', reverse('office_furniture_armchairs', args=('personel',))),
        (u'Для менеджеров', reverse('office_furniture_armchairs', args=('managers',))),
    )
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def office_furniture_armchairs(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Офисная мебель') & Q(module_mebel=u'Кресло'))
    if type == 'chief':
        products = products.filter(Q(armchaire_role=u'Для руководителя'))
        category_name = u'Офисная мебель - Кресла - Для руководителя'
    elif type == 'personel':
        products = products.filter(Q(armchaire_role=u'Для персонала'))
        category_name = u'Офисная мебель - Кресла - Для персонала'
    elif type == 'managers':
        products = products.filter(Q(armchaire_role=u'Для менеджеров'))
        category_name = u'Офисная мебель - Кресла - Для менеджеров'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def office_furniture_chairs_base(request, template_name="catalog/category.html"):
    category_name = u'Офисная мебель - Стулья'
    products = Product.active.filter(Q(komplekt_mebel=u'Офисная мебель') & Q(module_mebel=u'Стул'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def office_furniture_divider_base(request, template_name="catalog/category.html"):
    category_name = u'Офисная мебель - Перегородки'
    subcategories = (
        (u'Ресепшн', reverse('office_furniture_divider')),
    )
    products = Product.active.filter(Q(komplekt_mebel=u'Офисная мебель') & Q(module_mebel=u'Перегородка'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def office_furniture_divider(request, template_name="catalog/category.html"):
    category_name = u'Офисная мебель - Перегородки - Ресепшн'
    products = Product.active.filter(Q(komplekt_mebel=u'Офисная мебель') & Q(module_mebel=u'Ресепшн'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


############################ Камины ###########################

def fireplace_base(request, template_name="catalog/category.html"):
    category_name = u'Камины'
    subcategories = (
        (u'Каминные комплекты', reverse('fireplace_kamin_komplekt_base')),
        (u'Серии', reverse('fireplace_serii_komplekt_base')),
        (u'Порталы', reverse('fireplace_portals_base')),
        (u'Электрокамины', reverse('fireplace_electrokamins_base')),
        (u'Печи', reverse('fireplace_ovens')),
        (u'Аксессуары', reverse('fireplace_accesories')),
    )
    products = Product.active.filter(Q(module_komplekt=u'Камин'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def fireplace_kamin_komplekt_base(request, template_name="catalog/category.html"):
    category_name = u'Камины - Каминные комплекты'
    products = Product.active.filter(Q(komplekt_mebel=u'Каминный комплект'))
    subcategories = (
        (u'Выгодные', reverse('fireplace_kamin_komplekt', args=('vigodnie',))),
        (u'Stone', reverse('fireplace_kamin_komplekt', args=('stone',))),
        (u'New Look', reverse('fireplace_kamin_komplekt', args=('new_look',))),
        (u'Mini', reverse('fireplace_kamin_komplekt', args=('mini',))),
    )
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def fireplace_kamin_komplekt(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Каминный комплект'))
    if type == 'vigodnie':
        products = products.filter(Q(is_featured=True))
        category_name = u'Камины - Каминные комплекты - Выгодные'
    elif type == 'stone':
        products = products.filter(Q(brand=u'Stone'))
        category_name = u'Камины - Каминные комплекты - Stone'
    elif type == 'new_look':
        products = products.filter(Q(brand=u'New Look'))
        category_name = u'Камины - Каминные комплекты - New Look'
    elif type == 'mini':
        products = products.filter(Q(brand=u'Mini'))
        category_name = u'Камины - Каминные комплекты - Mini'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def fireplace_serii_komplekt_base(request, template_name="catalog/category.html"):
    category_name = u'Камины - Серии'
    products = Product.active.filter(Q(komplekt_mebel=u'Каминный комплект'))
    subcategories = (
        (u'Castle', reverse('fireplace_serii', args=('castle',))),
        (u'Stone', reverse('fireplace_serii', args=('stone',))),
        (u'Classic', reverse('fireplace_serii', args=('classic',))),
        (u'New Look', reverse('fireplace_serii', args=('new_look',))),
        (u'Mini', reverse('fireplace_serii', args=('mini',))),
        (u'Marble', reverse('fireplace_serii', args=('marble',))),
    )
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def fireplace_serii(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Каминный комплект'))
    if type == 'castle':
        products = products.filter(Q(brand=u'Castle'))
        category_name = u'Камины - Серии - Castle'
    elif type == 'stone':
        products = products.filter(Q(brand=u'Stone'))
        category_name = u'Камины - Серии - Stone'
    elif type == 'classic':
        products = products.filter(Q(brand=u'Classic'))
        category_name = u'Камины - Серии - Classic'
    elif type == 'new_look':
        products = products.filter(Q(brand=u'New Look'))
        category_name = u'Камины - Серии - New Look'
    elif type == 'mini':
        products = products.filter(Q(brand=u'Mini'))
        category_name = u'Камины - Серии - Mini'
    elif type == 'marble':
        products = products.filter(Q(brand=u'Marble'))
        category_name = u'Камины - Серии - Marble'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def fireplace_portals_base(request, template_name="catalog/category.html"):
    category_name = u'Камины - Порталы'
    subcategories = (
        (u'Натуральный мрамор', reverse('fireplace_portals', args=('natural_marble',))),
        (u'Полимерный камень', reverse('fireplace_portals', args=('polimer_stone',))),
        (u'МДФ', reverse('fireplace_portals', args=('mdf',))),
    )
    products = Product.active.filter(Q(module_other=u'Камин-портал'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def fireplace_portals(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_other=u'Камин-портал'))
    if type == 'natural_marble':
        products = products.filter(Q(material__name=u'Натуральный мрамор'))
        category_name = u'Камины - Порталы - Натуральный мрамор'
    elif type == 'polimer_stone':
        products = products.filter(Q(material__name=u'Полимерный камень'))
        category_name = u'Камины - Порталы - Полимерный камень'
    elif type == 'mdf':
        products = products.filter(Q(material__name=u'МДФ'))
        category_name = u'Камины - Порталы - МДФ'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def fireplace_electrokamins_base(request, template_name="catalog/category.html"):
    category_name = u'Камины - Электрокамины'
    subcategories = (
        (u'Широкий очаг', reverse('fireplace_electrokamins', args=('wide_flame',))),
        (u'Стандартный очаг', reverse('fireplace_electrokamins', args=('standard_flame',))),
        (u'Навесной очаг', reverse('fireplace_electrokamins', args=('hover_flame',))),
    )
    products = Product.active.filter(Q(module_other=u'Камин-электрокамин'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def fireplace_electrokamins(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_other=u'Камин-электрокамин'))
    if type == 'wide_flame':
        products = products.filter(Q(ochag=u'Широкий очаг'))
        category_name = u'Камины - Электрокамины - Широкий очаг'
    elif type == 'standard_flame':
        products = products.filter(Q(ochag=u'Стандартный очаг'))
        category_name = u'Камины - Электрокамины - Стандартный очаг'
    elif type == 'hover_flame':
        products = products.filter(Q(ochag=u'Навесной очаг'))
        category_name = u'Камины - Электрокамины - Навесной очаг'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def fireplace_ovens(request, template_name="catalog/category.html"):
    category_name = u'Камины - Камин-печь'
    products = Product.active.filter(Q(module_other=u'Камин-печь'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def fireplace_accesories(request, template_name="catalog/category.html"):
    category_name = u'Камины - Аксессуары'
    products = Product.active.filter(Q(module_other=u'Камин-аксессуар'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


######################### Столы ################################
def tables_base(request, template_name="catalog/category.html"):
    category_name = u'Столы'
    subcategories = (
        (u'Раскладные', reverse('tables_foldable_base')),
        (u'Не раскладные', reverse('tables_unfoldable_base')),
    )
    products = Product.active.filter(Q(module_mebel=u'Стол'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def tables_foldable_base(request, template_name="catalog/category.html"):
    category_name = u'Столы - Раскладные'
    subcategories = (
        (u'Деревянные', reverse('tables_foldable_wooden_base')),
        (u'Стеклянные', reverse('tables_foldable_glass_base')),
        (u'ЛДСП', reverse('tables_foldable_ldsp_base')),
        (u'Другие', reverse('tables_foldable_others_base')),
    )
    products = Product.active.filter(Q(module_mebel=u'Стол'))
    products = products.filter(Q(architecture_type__name=u'Раскладные'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def tables_foldable_wooden_base(request, template_name="catalog/category.html"):
    category_name = u'Столы - Раскладные - Деревянные'
    subcategories = (
        (u'Круглые', reverse('tables_foldable', args=('wooden', 'round'))),
        (u'Овальные', reverse('tables_foldable', args=('wooden', 'oval'))),
        (u'Прямоугольные', reverse('tables_foldable', args=('wooden', 'rectangle'))),
        (u'Другие', reverse('tables_foldable', args=('wooden', 'others'))),
    )
    products = Product.active.filter(Q(module_mebel=u'Стол'))
    products = products.filter(Q(architecture_type__name=u'Раскладные'))
    products = products.filter(Q(material__name=u'Деревянные'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def tables_foldable_glass_base(request, template_name="catalog/category.html"):
    category_name = u'Столы - Раскладные - Стеклянные'
    subcategories = (
        (u'Круглые', reverse('tables_foldable', args=('glass', 'round'))),
        (u'Овальные', reverse('tables_foldable', args=('glass', 'oval'))),
        (u'Прямоугольные', reverse('tables_foldable', args=('glass', 'rectangle'))),
        (u'Другие', reverse('tables_foldable', args=('glass', 'others'))),
    )
    products = Product.active.filter(Q(module_mebel=u'Стол'))
    products = products.filter(Q(architecture_type__name=u'Раскладные'))
    products = products.filter(Q(material__name=u'Стеклянные'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def tables_foldable_ldsp_base(request, template_name="catalog/category.html"):
    category_name = u'Столы - Раскладные - ЛДСП'
    subcategories = (
        (u'Круглые', reverse('tables_foldable', args=('ldsp', 'round'))),
        (u'Овальные', reverse('tables_foldable', args=('ldsp', 'oval'))),
        (u'Прямоугольные', reverse('tables_foldable', args=('ldsp', 'rectangle'))),
        (u'Другие', reverse('tables_foldable', args=('ldsp', 'others'))),
    )
    products = Product.active.filter(Q(module_mebel=u'Стол'))
    products = products.filter(Q(architecture_type__name=u'Раскладные'))
    products = products.filter(Q(material__name=u'ЛДСП'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def tables_foldable_others_base(request, template_name="catalog/category.html"):
    category_name = u'Столы - Раскладные - Другие'
    subcategories = (
        (u'Офисные', reverse('tables_foldable', args=('others', 'office'))),
        (u'Ротанг', reverse('tables_foldable', args=('others', 'rotang'))),
        (u'Садовые', reverse('tables_foldable', args=('others', 'garden'))),
    )
    products = Product.active.filter(Q(module_mebel=u'Стол'))
    products = products.filter(Q(architecture_type__name=u'Раскладные'))
    products = products.filter(~Q(material__name=u'Деревянные') & ~Q(material__name=u'Стеклянные') & ~Q(material__name=u'ЛДСП'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def tables_foldable(request, type1, type2, template_name="catalog/category.html"):
    category_name = u'Столы - Раскладные'
    products = Product.active.filter(Q(module_mebel=u'Стол'))
    products = products.filter(Q(architecture_type__name=u'Раскладные'))
    if type1 == 'wooden':
        products = products.filter(Q(material__name=u'Деревянные'))
        category_name += u' - Деревянные'
    elif type1 == 'glass':
        products = products.filter(Q(material__name=u'Стеклянные'))
        category_name += u' - Стеклянные'
    elif type1 == 'ldsp':
        products = products.filter(Q(material__name=u'ЛДСП'))
        category_name += u' - ЛДСП'
    elif type1 == 'others':
        products = products.filter(
            ~Q(material__name=u'Деревянные') & ~Q(material__name=u'Стеклянные') & ~Q(material__name=u'ЛДСП'))
        category_name += u' - Другие'
    if type2 == 'round':
        products = products.filter(Q(shape=u'Круглые'))
        category_name += u' - Круглые'
    elif type2 == 'oval':
        products = products.filter(Q(shape=u'Овальные'))
        category_name += u' - Овальные'
    elif type2 == 'rectangle':
        products = products.filter(Q(shape=u'Прямоугольные'))
        category_name += u' - Прямоугольные'
    elif type2 == 'others':
        products = products.filter(~Q(shape=u'Круглые') & ~Q(shape=u'Овальные') & ~Q(shape=u'Прямоугольные'))
        category_name += u' - Другие'
    elif type2 == 'office':
        products = products.filter(Q(architecture_type__name=u'Офисные') | Q(style=u'Офисные'))
        category_name += u' - Офисные'
    elif type2 == 'rotang':
        products = products.filter(Q(material__name__icontains=u'Ротанг'))
        category_name += u' - Ротанг'
    elif type2 == 'garden':
        products = products.filter(Q(style=u'Садовые'))
        category_name += u' - Садовые'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def tables_unfoldable_base(request, template_name="catalog/category.html"):
    category_name = u'Столы - Не раскладные'
    products = Product.active.filter(Q(module_mebel=u'Стол'))
    products = products.filter(~Q(architecture_type__name=u'Раскладные'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def tables_unfoldable_wooden_base(request, template_name="catalog/category.html"):
    category_name = u'Столы - Не раскладные - Деревянные'
    subcategories = (
        (u'Круглые', reverse('tables_unfoldable', args=('wooden', 'round'))),
        (u'Овальные', reverse('tables_unfoldable', args=('wooden', 'oval'))),
        (u'Прямоугольные', reverse('tables_unfoldable', args=('wooden', 'rectangle'))),
        (u'Другие', reverse('tables_unfoldable', args=('wooden', 'others'))),
    )
    products = Product.active.filter(Q(module_mebel=u'Стол'))
    products = products.filter(~Q(architecture_type__name=u'Раскладные'))
    products = products.filter(Q(material__name=u'Деревянные'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def tables_unfoldable_glass_base(request, template_name="catalog/category.html"):
    category_name = u'Столы - Не раскладные - Стеклянные'
    subcategories = (
        (u'Круглые', reverse('tables_unfoldable', args=('glass', 'round'))),
        (u'Овальные', reverse('tables_unfoldable', args=('glass', 'oval'))),
        (u'Прямоугольные', reverse('tables_unfoldable', args=('glass', 'rectangle'))),
        (u'Другие', reverse('tables_unfoldable', args=('glass', 'others'))),
    )
    products = Product.active.filter(Q(module_mebel=u'Стол'))
    products = products.filter(~Q(architecture_type__name=u'Раскладные'))
    products = products.filter(Q(material__name=u'Стеклянные'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def tables_unfoldable_ldsp_base(request, template_name="catalog/category.html"):
    category_name = u'Столы - Не раскладные - ЛДСП'
    subcategories = (
        (u'Круглые', reverse('tables_unfoldable', args=('ldsp', 'round'))),
        (u'Овальные', reverse('tables_unfoldable', args=('ldsp', 'oval'))),
        (u'Прямоугольные', reverse('tables_unfoldable', args=('ldsp', 'rectangle'))),
        (u'Другие', reverse('tables_unfoldable', args=('ldsp', 'others'))),
    )
    products = Product.active.filter(Q(module_mebel=u'Стол'))
    products = products.filter(~Q(architecture_type__name=u'Раскладные'))
    products = products.filter(Q(material__name=u'ЛДСП'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def tables_unfoldable_others_base(request, template_name="catalog/category.html"):
    category_name = u'Столы - Не раскладные - Другие'
    subcategories = (
        (u'Офисные', reverse('tables_unfoldable', args=('others', 'office'))),
        (u'Ротанг', reverse('tables_unfoldable', args=('others', 'rotang'))),
        (u'Садовые', reverse('tables_unfoldable', args=('others', 'garden'))),
    )
    products = Product.active.filter(Q(module_mebel=u'Стол'))
    products = products.filter(~Q(architecture_type__name=u'Раскладные'))
    products = products.filter(~Q(material__name=u'Деревянные') & ~Q(material__name=u'Стеклянные') & ~Q(material__name=u'ЛДСП'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def tables_unfoldable(request, type1, type2, template_name="catalog/category.html"):
    category_name = u'Столы - Не раскладные'
    products = Product.active.filter(Q(module_mebel=u'Стол'))
    products = products.filter(~Q(architecture_type__name=u'Раскладные'))
    if type1 == 'wooden':
        products = products.filter(Q(material__name=u'Деревянные'))
        category_name += u' - Деревянные'
    elif type1 == 'glass':
        products = products.filter(Q(material__name=u'Стеклянные'))
        category_name += u' - Стеклянные'
    elif type1 == 'ldsp':
        products = products.filter(Q(material__name=u'ЛДСП'))
        category_name += u' - ЛДСП'
    elif type1 == 'others':
        products = products.filter(
            ~Q(material__name=u'Деревянные') & ~Q(material__name=u'Стеклянные') & ~Q(material__name=u'ЛДСП'))
        category_name += u' - Другие'
    if type2 == 'round':
        products = products.filter(Q(shape=u'Круглые'))
        category_name += u' - Круглые'
    elif type2 == 'oval':
        products = products.filter(Q(shape=u'Овальные'))
        category_name += u' - Овальные'
    elif type2 == 'rectangle':
        products = products.filter(Q(shape=u'Прямоугольные'))
        category_name += u' - Прямоугольные'
    elif type2 == 'others':
        products = products.filter(~Q(shape=u'Круглые') & ~Q(shape=u'Овальные') & ~Q(shape=u'Прямоугольные'))
        category_name += u' - Другие'
    elif type2 == 'office':
        products = products.filter(Q(architecture_type__name=u'Офисные') | Q(style=u'Офисные'))
        category_name += u' - Офисные'
    elif type2 == 'rotang':
        products = products.filter(Q(material__name__icontains=u'Ротанг'))
        category_name += u' - Ротанг'
    elif type2 == 'garden':
        products = products.filter(Q(style=u'Садовые'))
        category_name += u' - Садовые'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


############################# Стулья ################################

def chairs_base(request, template_name="catalog/category.html"):
    category_name = u'Стулья'
    subcategories = (
        (u'Деревянные', reverse('chairs_wooden')),
        (u'Металлокаркас', reverse('chairs_metalkarkas')),
        (u'Пластиковые', reverse('chairs_plastic')),
        (u'Разные', reverse('chairs_others_base')),
        (u'Барные', reverse('chairs_barniy')),
        (u'Складные', reverse('chairs_foldable')),
    )
    products = Product.active.filter(Q(module_mebel=u'Стул'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def chairs_wooden(request, template_name="catalog/category.html"):
    category_name = u'Стулья - Деревянные'
    products = Product.active.filter(Q(module_mebel=u'Стул'))
    products = products.filter(Q(material__name=u'Деревянные'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def chairs_metalkarkas(request, template_name="catalog/category.html"):
    category_name = u'Стулья - Металлокаркас'
    products = Product.active.filter(Q(module_mebel=u'Стул'))
    products = products.filter(Q(material__name=u'Металлокаркас'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def chairs_plastic(request, template_name="catalog/category.html"):
    category_name = u'Стулья - Пластиковые'
    products = Product.active.filter(Q(module_mebel=u'Стул'))
    products = products.filter(Q(material__name=u'Пластиковые'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def chairs_barniy(request, template_name="catalog/category.html"):
    category_name = u'Стулья - Барные'
    products = Product.active.filter(Q(module_mebel=u'Стул'))
    products = products.filter(Q(style=u'Для баров и ресторанов'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def chairs_foldable(request, template_name="catalog/category.html"):
    category_name = u'Стулья - Складные'
    products = Product.active.filter(Q(module_mebel=u'Стул'))
    products = products.filter(Q(architecture_type__name=u'Раскладные'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def chairs_others_base(request, template_name="catalog/category.html"):
    category_name = u'Стулья - Разные'
    subcategories = (
        (u'Ротанг', reverse('chairs_others', args=('rotang',))),
        (u'Офисные', reverse('chairs_others', args=('rotang',))),
        (u'Для кинотеатров', reverse('chairs_others', args=('rotang',))),
        (u'Для посетителей', reverse('chairs_others', args=('rotang',))),
    )
    products = Product.active.filter(Q(module_mebel=u'Стул'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def chairs_others(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_mebel=u'Стул'))
    if type == 'rotang':
        products = products.filter(Q(rotang=True))
        category_name = u'Стулья - Разные - Ротанг'
    elif type == 'office':
        products = products.filter(Q(architecture_type__name=u'Офисные') | Q(style=u'Офисные'))
        category_name = u'Стулья - Разные - Офисные'
    elif type == 'cinema':
        products = products.filter(Q(style=u'Для кинотеатров'))
        category_name = u'Стулья - Разные - Для кинотеатров'
    elif type == 'visitors':
        products = products.filter(Q(style=u'Для посетителей'))
        category_name = u'Стулья - Разные - Для посетителей'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


############################ Кухонные уголки #################################

def kitchen_corners_base(request, template_name="catalog/category.html"):
    category_name = u'Кухонные уголки'
    subcategories = (
        (u'Комплекты', reverse('kitchen_corners_komplekts_base')),
        (u'Модульно', reverse('kitchen_corners_module_base')),
        (u'Кухонные + угловые диваны', reverse('kitchen_corner_sofa_base')),
        (u'Уголки от', reverse('kitchen_corner_from')),
    )
    products = Product.active.filter(Q(komplekt_mebel=u'Кухонный уголок') | Q(module_mebel=u'Кухонный уголок'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def kitchen_corners_komplekts_base(request, template_name="catalog/category.html"):
    category_name = u'Кухонные уголки - Комплекты'
    subcategories = (
        (u'Деревянные', reverse('kitchen_corners_komplekts', args=('wooden',))),
        (u'ЛДСП', reverse('kitchen_corners_komplekts', args=('ldsp',))),
        (u'Металлокаркас', reverse('kitchen_corners_komplekts', args=('metalkarkas',))),
    )
    products = Product.active.filter(Q(module_komplekt=u'Комплект'))
    products = products.filter(Q(komplekt_mebel=u'Кухонный уголок'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def kitchen_corners_komplekts(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_komplekt=u'Комплект'))
    products = products.filter(Q(komplekt_mebel=u'Кухонный уголок'))
    if type == 'wooden':
        products = products.filter(Q(material__name=u'Деревянные'))
        category_name = u'Кухонные уголки - Комплекты - Деревянные'
    elif type == 'ldsp':
        products = products.filter(Q(material__name=u'ЛДСП'))
        category_name = u'Кухонные уголки - Комплекты - ЛДСП'
    elif type == 'metalkarkas':
        products = products.filter(Q(material__name=u'Металлокаркас'))
        category_name = u'Кухонные уголки - Комплекты - Металлокаркас'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def kitchen_corners_module_base(request, template_name="catalog/category.html"):
    category_name = u'Кухонные уголки - Модули'
    subcategories = (
        (u'Деревянные', reverse('kitchen_corners_module_wooden')),
        (u'ЛДСП', reverse('kitchen_corners_module_ldsp')),
        (u'Металлокаркас', reverse('kitchen_corners_module_metalkarkas')),
    )
    products = Product.active.filter(Q(module_komplekt=u'Модуль'))
    products = products.filter(Q(module_mebel=u'Кухонный уголок'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def kitchen_corners_module_wooden(request, template_name="catalog/category.html"):
    category_name = u'Кухонные уголки - Модули - Деревянные'
    subcategories = (
        (u'Столы', reverse('kitchen_corners_module', args=('wooden', 'tables',))),
        (u'Стулья', reverse('kitchen_corners_module', args=('wooden', 'chairs',))),
        (u'Уголки', reverse('kitchen_corners_module', args=('wooden', 'corners',))),
    )
    products = Product.active.filter(Q(module_komplekt=u'Модуль'))
    products = products.filter(Q(module_mebel=u'Кухонный уголок'))
    products = products.filter(Q(material__name=u'Деревянные'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def kitchen_corners_module_ldsp(request, template_name="catalog/category.html"):
    category_name = u'Кухонные уголки - Модули - ЛДСП'
    subcategories = (
        (u'Столы', reverse('kitchen_corners_module', args=('ldsp', 'tables',))),
        (u'Стулья', reverse('kitchen_corners_module', args=('ldsp', 'chairs',))),
        (u'Уголки', reverse('kitchen_corners_module', args=('ldsp', 'corners',))),
    )
    products = Product.active.filter(Q(module_komplekt=u'Модуль'))
    products = products.filter(Q(module_mebel=u'Кухонный уголок'))
    products = products.filter(Q(material__name=u'ЛДСП'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def kitchen_corners_module_metalkarkas(request, template_name="catalog/category.html"):
    category_name = u'Кухонные уголки - Модули - Металлокаркас'
    subcategories = (
        (u'Столы', reverse('kitchen_corners_module', args=('metalkarkas', 'tables',))),
        (u'Стулья', reverse('kitchen_corners_module', args=('metalkarkas', 'chairs',))),
        (u'Уголки', reverse('kitchen_corners_module', args=('metalkarkas', 'corners',))),
    )
    products = Product.active.filter(Q(module_komplekt=u'Модуль'))
    products = products.filter(Q(module_mebel=u'Кухонный уголок'))
    products = products.filter(Q(material__name=u'Металлокаркас'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def kitchen_corners_module(request, type1, type2, template_name="catalog/category.html"):
    category_name = u'Кухонные уголки - Модули'
    products = Product.active.filter(Q(module_komplekt=u'Модуль'))
    products = products.filter(Q(module_mebel=u'Кухонный уголок'))
    if type1 == 'wooden':
        products = products.filter(Q(material__name=u'Деревянные'))
        category_name += u' - Деревянные'
    elif type1 == 'ldsp':
        products = products.filter(Q(material__name=u'ЛДСП'))
        category_name += u' - ЛДСП'
    elif type1 == 'metalkarkas':
        products = products.filter(Q(material__name=u'Металлокаркас'))
        category_name += u' - Металлокаркас'
    if type2 == 'tables':
        products = products.filter(Q(module_mebel=u'Стол'))
        category_name += u' - Стол'
    elif type2 == 'chairs':
        products = products.filter(Q(module_mebel=u'Стул'))
        category_name += u' - Стул'
    elif type2 == 'corners':
        products = products.filter(Q(module_mebel=u'Кухонный уголок'))
        category_name += u' - Кухонный уголок'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def kitchen_corner_sofa_base(request, type, template_name="catalog/category.html"):
    category_name = u'Кухонные уголки - Кухонные + угловые диваны'
    subcategories = (
        (u'Раскладные', reverse('kitchen_corner_sofa', args=('foldable',))),
        (u'Не раскладные', reverse('kitchen_corner_sofa', args=('unfoldable',))),
    )
    products = Product.active.filter(Q(module_mebel=u'Диван'))
    products = products.filter(Q(room=u'Кухня'))
    products = products.filter(Q(shape=u'Угловые'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def kitchen_corner_sofa(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_mebel=u'Диван'))
    products = products.filter(Q(room=u'Кухня'))
    products = products.filter(Q(shape=u'Угловые'))
    if type == 'foldable':
        products = products.filter(Q(architecture_type__name=u'Раскладные'))
        category_name = u'Кухонные уголки - Кухонные + угловые диваны - Раскладные'
    elif type == 'unfoldable':
        products = products.filter(~Q(architecture_type__name=u'Раскладные'))
        category_name = u'Кухонные уголки - Кухонные + угловые диваны - Не раскладные'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def kitchen_corner_from(request, template_name="catalog/category.html"):
    category_name = u'Кухонные уголки - Кухонные + угловые диваны - Уголки от'
    products = Product.active.filter(Q(shape=u'Угловые'))
    products = products.filter(Q(room=u'Кухня'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


########################### Матрасы ##############################

def matrasses_base(request, template_name="catalog/category.html"):
    category_name = u'Матрасы'
    subcategories = (
        (u'Пружинные', reverse('matrasses', args=('springing',))),
        (u'Ортопедические', reverse('matrasses', args=('ortoped',))),
        (u'Анатомические', reverse('matrasses', args=('anatom',))),
    )
    products = Product.active.filter(Q(module_mebel=u'Матрас'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def matrasses(request, type, template_name="catalog/category.html"):
    category_name = u'Матрас'
    products = Product.active.filter(Q(module_mebel=category_name))
    if type == 'springing':
        products = products.filter(Q(architecture_type__name=u'Пружинные'))
        category_name = u'Матрасы - Пружинные'
    elif type == 'ortoped':
        products = products.filter(Q(architecture_type__name=u'Ортопедические'))
        category_name = u'Матрасы - Ортопедические'
    elif type == 'anatom':
        products = products.filter(Q(architecture_type__name=u'Анатомические'))
        category_name = u'Матрасы - Анатомические'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


########################## Садовая мебель #############################

def garden_furniture_base(request, template_name="catalog/category.html"):
    category_name = u'Садовая мебель'
    subcategories = (
        (u'Ротанг', reverse('garden_furniture_rotang_base')),
        (u'Качели', reverse('garden_furniture_kacheli')),
        (u'Раскладушки', reverse('garden_furniture_raskladushka')),
        (u'Кресла', reverse('garden_furniture_armchair')),
        (u'Шезлонги', reverse('garden_furniture_shezlong')),
        (u'Другое', reverse('garden_furniture_others')),
    )
    products = Product.active.filter(Q(style=u'Садовые'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def garden_furniture_rotang_base(request, template_name="catalog/category.html"):
    category_name = u'Садовая мебель - Ротанг'
    subcategories = (
        (u'Искусственный', reverse('garden_furniture_rotang_artificial')),
        (u'Натуральный', reverse('garden_furniture_rotang_natural')),
        (u'Дерево', reverse('garden_furniture_rotang_wooden')),
    )
    products = Product.active.filter(Q(style=u'Садовые'))
    products = products.filter(Q(material__name__icontains=u'Ротанг'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def garden_furniture_rotang_artificial(request, template_name="catalog/category.html"):
    category_name = u'Садовая мебель - Ротанг - Искусственный'
    subcategories = (
        (u'Диваны', reverse('garden_furniture_rotang_material', args=('artificial', 'sofas'))),
        (u'Столы', reverse('garden_furniture_rotang_material', args=('artificial', 'tables'))),
        (u'Кресла', reverse('garden_furniture_rotang_material', args=('artificial', 'armchairs'))),
        (u'Стулья', reverse('garden_furniture_rotang_material', args=('artificial', 'chairs'))),
    )
    products = Product.active.filter(Q(style=u'Садовые'))
    products = products.filter(Q(material__name=u'Ротанг искусственный'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def garden_furniture_rotang_natural(request, template_name="catalog/category.html"):
    category_name = u'Садовая мебель - Ротанг - Натуральный'
    subcategories = (
        (u'Диваны', reverse('garden_furniture_rotang_material', args=('natural', 'sofas'))),
        (u'Столы', reverse('garden_furniture_rotang_material', args=('natural', 'tables'))),
        (u'Кресла', reverse('garden_furniture_rotang_material', args=('natural', 'armchairs'))),
        (u'Стулья', reverse('garden_furniture_rotang_material', args=('natural', 'chairs'))),
    )
    products = Product.active.filter(Q(style=u'Садовые'))
    products = products.filter(Q(material__name=u'Ротанг натуральный'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def garden_furniture_rotang_wooden(request, template_name="catalog/category.html"):
    category_name = u'Садовая мебель - Ротанг - Дерево'
    subcategories = (
        (u'Диваны', reverse('garden_furniture_rotang_material', args=('wooden', 'sofas'))),
        (u'Столы', reverse('garden_furniture_rotang_material', args=('wooden', 'tables'))),
        (u'Кресла', reverse('garden_furniture_rotang_material', args=('wooden', 'armchairs'))),
        (u'Стулья', reverse('garden_furniture_rotang_material', args=('wooden', 'chairs'))),
    )
    products = Product.active.filter(Q(style=u'Садовые'))
    products = products.filter(Q(material__name=u'Деревянные'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def garden_furniture_rotang_material(request, type1, type2, template_name="catalog/category.html"):
    category_name = u'Садовая мебель - Ротанг'
    products = Product.active.filter(Q(style=u'Садовые'))
    products = products.filter(Q(material__name__icontains=u'Ротанг'))
    if type1 == 'artificial':
        products = products.filter(Q(material__name=u'Ротанг искусственный'))
        category_name += u' - Ротанг искусственный'
    elif type1 == 'natural':
        products = products.filter(Q(material__name=u'Ротанг натуральный'))
        category_name += u' - Ротанг натуральный'
    elif type1 == 'wooden':
        products = products.filter(Q(material__name=u'Деревянные'))
        category_name += u' - Дерево'
    if type2 == 'sofas':
        products = products.filter(Q(module_mebel=u'Диван'))
        category_name += u' - Диваны'
    elif type2 == 'tables':
        products = products.filter(Q(module_mebel=u'Стол'))
        category_name += u' - Столы'
    elif type2 == 'armchairs':
        products = products.filter(Q(module_mebel=u'Кресло'))
        category_name += u' - Кресла'
    elif type2 == 'chairs':
        products = products.filter(Q(module_mebel=u'Стул'))
        category_name += u' - Стулья'
    subcategories = (
        (u'Мини', reverse('garden_furniture_rotang', args=(type1, type2, 'mini'))),
        (u'Стандарт', reverse('garden_furniture_rotang', args=(type1, type2, 'standard'))),
    )
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def garden_furniture_rotang(request, type1, type2, type3, template_name="catalog/category.html"):
    products = Product.active.filter(Q(style=u'Садовые'))
    products = products.filter(Q(material__name__icontains=u'Ротанг'))
    if type1 == 'artificial':
        products = products.filter(Q(material__name=u'Ротанг искусственный'))
    elif type1 == 'natural':
        products = products.filter(Q(material__name=u'Ротанг натуральный'))
    elif type1 == 'wooden':
        products = products.filter(Q(material__name=u'Деревянные'))
    if type2 == 'sofas':
        products = products.filter(Q(module_mebel=u'Диван'))
    elif type2 == 'tables':
        products = products.filter(Q(module_mebel=u'Стол'))
    elif type2 == 'armchairs':
        products = products.filter(Q(module_mebel=u'Кресло'))
    elif type2 == 'chairs':
        products = products.filter(Q(module_mebel=u'Стул'))
    if type3 == 'mini':
        products = products.filter(Q(architecture_type__name=u'Мини'))
    elif type3 == 'standard':
        products = products.filter(Q(architecture_type__name=u'Стандарт'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def garden_furniture_kacheli(request, template_name="catalog/category.html"):
    products = Product.active.filter(Q(style=u'Садовые'))
    products = products.filter(Q(module_other=u'Качели'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def garden_furniture_raskladushka(request, template_name="catalog/category.html"):
    products = Product.active.filter(Q(style=u'Садовые'))
    products = products.filter(Q(module_other=u'Раскладушка'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def garden_furniture_armchair(request, template_name="catalog/category.html"):
    products = Product.active.filter(Q(style=u'Садовые'))
    products = products.filter(Q(module_mebel=u'Кресло'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def garden_furniture_shezlong(request, template_name="catalog/category.html"):
    products = Product.active.filter(Q(style=u'Садовые'))
    products = products.filter(Q(module_other=u'Шезлонг'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def garden_furniture_others(request, template_name="catalog/category.html"):
    products = Product.active.filter(Q(style=u'Садовые'))
    products = products.filter(Q(rotang=False) &
                               ~Q(module_other=u'Качели') &
                               ~Q(module_other=u'Раскладушка') &
                               ~Q(module_mebel=u'Кресло') &
                               ~Q(module_other=u'Шезлонг')
                               )
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


################## Для баров и ресторанов #####################

def bars_restaurants_base(request, template_name="catalog/category.html"):
    category_name = u'Для баров и ресторанов'
    subcategories = (
        (u'Столы', reverse('bars_restaurants', args=('tables',))),
        (u'Стулья', reverse('bars_restaurants', args=('chairs',))),
        (u'Диваны', reverse('bars_restaurants', args=('sofas',))),
        (u'Под старину', reverse('bars_restaurants', args=('vintage',))),
        (u'Стойки', reverse('bars_restaurants', args=('stoyki',))),
    )
    products = Product.active.filter(Q(style=u'Для баров и ресторанов'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def bars_restaurants(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(style=u'Для баров и ресторанов'))
    if type == 'tables':
        products = products.filter(Q(module_mebel=u'Стол'))
        category_name = u'Для баров и ресторанов - Столы'
    elif type == 'chairs':
        products = products.filter(Q(module_mebel=u'Стул'))
        category_name = u'Для баров и ресторанов - Стулья'
    elif type == 'sofas':
        products = products.filter(Q(module_mebel=u'Диван'))
        category_name = u'Для баров и ресторанов - Диваны'
    elif type == 'vintage':
        products = products.filter(Q(style=u'Под старину'))
        category_name = u'Для баров и ресторанов - Под старину'
    elif type == 'stoyki':
        products = products.filter(Q(module_mebel=u'Стойка'))
        category_name = u'Для баров и ресторанов - Стойки'
        subcategories = (
            (u'Прилавки', reverse('bars_restaurants_prilavki')),
        )
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def bars_restaurants_prilavki(request, template_name="catalog/category.html"):
    category_name = u'Для баров и ресторанов - Стойки - Прилавки'
    products = Product.active.filter(Q(style=u'Для баров и ресторанов'))
    products = products.filter(Q(module_mebel=u'Прилавок'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


############################## Шкафы-купе ##############################

def case_kupe(request, template_name="catalog/category.html"):
    category_name = u'Шкафы-купе'
    products = Product.active.filter(Q(architecture_type__name=u'Шкаф-купе'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


######################## Гостиничные номера ##############################

def hotels(request, template_name="catalog/category.html"):
    category_name = u'Гостиничные номера'
    products = Product.active.filter(Q(style=u'Гостиничные номера'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


###################### Интерьер ############################

def interier_base(request, template_name="catalog/category.html"):
    category_name = u'Интерьер'
    subcategories = (
        (u'Цветы', reverse('interier', args=('flowers',))),
        (u'Статуэтки', reverse('interier', args=('statues',))),
        (u'Картины', reverse('interier', args=('pictures',))),
        (u'Вазы', reverse('interier', args=('vases',))),
        (u'Корзины', reverse('interier', args=('buckets',))),
    )
    products = Product.active.filter(Q(module_komplekt=u'Интерьер'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def interier(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_komplekt=u'Интерьер'))
    if type == 'flowers':
        products = products.filter(Q(module_other=u'Цветы'))
        category_name = u'Интерьер - Цветы'
    elif type == 'statues':
        products = products.filter(Q(module_other=u'Статуэтка'))
        category_name = u'Интерьер - Статуэтки'
    elif type == 'pictures':
        products = products.filter(Q(module_other=u'Картина'))
        category_name = u'Интерьер - Картины'
    elif type == 'buckets':
        products = products.filter(Q(module_other=u'Корзина'))
        category_name = u'Интерьер - Корзины'
        subcategories = (
            (u'Сундуки', reverse('interier_buckets')),
        )
    elif type == 'vases':
        products = products.filter(Q(module_other=u'Вазы'))
        category_name = u'Интерьер - Вазы'
        subcategories = (
            (u'Стекло', reverse('interier_vases', args=('glass',))),
            (u'Плетеные', reverse('interier_vases', args=('pletenie',))),
        )
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def interier_vases(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_komplekt=u'Интерьер'))
    products = products.filter(Q(module_other=u'Ваза'))
    if type == 'glass':
        products = products.filter(Q(material__name=u'Стеклянные'))
        category_name = u'Интерьер - Вазы - Стекло'
    elif type == 'pletenie':
        products = products.filter(Q(material__name=u'Плетеные'))
        category_name = u'Интерьер - Вазы - Плетеные'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def interier_buckets(request, template_name="catalog/category.html"):
    category_name = u'Интерьер - Корзины - Сундуки'
    products = Product.active.filter(Q(module_komplekt=u'Интерьер'))
    products = products.filter(Q(module_other=u'Сундук'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


######################## Разное ##############################

def others(request, template_name="catalog/category.html"):
    category_name = u'Разное'
    products = Product.active.filter(Q(module_other=u'Разное'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


######################## Сопутствующие товары ##############################

def associated_goods_base(request, template_name="catalog/category.html"):
    category_name = u'Сопутствующие товары'
    subcategories = (
        (u'Электротовары', reverse('associated_goods', args=('electronics',))),
        (u'Смесители', reverse('associated_goods', args=('smesitels',))),
        (u'Плиты', reverse('associated_goods', args=('stoves',))),
        (u'Холодильники', reverse('associated_goods', args=('refrigirators',))),
        (u'Мойки', reverse('associated_goods', args=('sinks',))),
        (u'Фартуки', reverse('associated_goods', args=('aprons',))),
    )
    products = Product.active.filter(Q(module_komplekt=u'Сопутствующие товары'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def associated_goods(request, type, template_name="catalog/category.html"):
    products = Product.active.all()
    if type == 'electronics':
        products = products.filter(Q(module_other=u'Электротовар'))
    elif type == 'smesitels':
        products = products.filter(Q(module_other=u'Смеситель'))
    elif type == 'stoves':
        products = products.filter(Q(module_other=u'Плита'))
    elif type == 'refrigirators':
        products = products.filter(Q(module_other=u'Холодильник'))
    elif type == 'sinks':
        products = products.filter(Q(module_other=u'Мойка'))
    elif type == 'aprons':
        products = products.filter(Q(module_other=u'Фартук'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


######################## Индивидуальные заказы ##############################

def individual_orders(request, template_name="catalog/category.html"):
    category_name = u'Индивидуальные заказы'
    products = Product.active.filter(Q(on_order=True))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


######################################################################


def show_product(request, product_slug, template_name="catalog/product.html"):
    p = get_object_or_404(Product, slug=product_slug)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    # need to evaluate the HTTP method
    if request.method == 'POST':
        # add to cart create the bound form
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request, postdata)
        # check if posted data is valid
        if form.is_valid():
            # add to cart and redirect to cart page
            cart.add_to_cart(request)
            # if test cookie worked, get rid of it
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            url = urlresolvers.reverse('show_cart')
            return HttpResponseRedirect(url)
    # its a GET,create the unbound form. Note request as a kwarg
    form = ProductAddToCartForm(request=request, label_suffix=':')
    # assign the hidden input the product slug
    form.fields['product_slug'].widget.attrs['value'] = product_slug
    # set the test cookie on our first GET request
    request.session.set_test_cookie()
    stats.log_product_view(request, p)  # add to product view
    product_reviews = ProductReview.approved.filter(product=p).order_by('-date')
    review_form = ProductReviewForm()
    # check if user is torgpred
    torgpred = False
    user = request.user
    if user.groups.filter(name=u'Торговые представители').exists():
        torgpred = True
    return render_to_response("catalog/product.html", locals(), context_instance=RequestContext(request))
