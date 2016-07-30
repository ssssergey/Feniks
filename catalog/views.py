# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render_to_response
from catalog.models import ProductReview, Product
from django.template import RequestContext
from django.db.models import Q
from django.core import urlresolvers
from cart import cart
from django.http import HttpResponseRedirect
from forms import ProductAddToCartForm, ProductReviewForm

from stats import stats
from Feniks.settings import PRODUCTS_PER_ROW

from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
import json
from django.http import HttpResponse


def index(request, template_name="catalog/index.html"):
    page_title = u'Феникс'
    # search_recs = stats.recommended_from_search(request)
    # featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
    # recently_viewed = stats.get_recently_viewed(request)
    # view_recs = stats.recommended_from_views(request)
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_kitchens(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель') & Q(room=u'Кухня'))
    if type == 'komplekts':
        products = products.filter(Q(module_komplekt=u'Комплект'))
    elif type == 'modules':
        products = products.filter(Q(module_komplekt=u'Модуль'))
    elif type == 'others':
        products = products.filter(Q(module_komplekt__isnull=True))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_gorki_stenki_gestrooms(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель') & Q(room=u'Гостиная(горки, стенки)'))
    if type == 'komplekts':
        products = products.filter(Q(module_komplekt=u'Комплект'))
    elif type == 'modules':
        products = products.filter(Q(module_komplekt=u'Модуль'))
    elif type == 'others':
        products = products.filter(Q(module_komplekt__isnull=True))
    elif type == 'libraries':
        products = products.filter(Q(module_mebel=u'Библиотека'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_bedrooms(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель') & Q(room=u'Спальня'))
    if type == 'komplekts':
        products = products.filter(Q(module_komplekt=u'Комплект'))
    elif type == 'modules':
        products = products.filter(Q(module_komplekt=u'Модуль'))
    elif type == 'others':
        products = products.filter(Q(module_komplekt__isnull=True))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_corridors(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель') & Q(room=u'Прихожие'))
    if type == 'komplekts':
        products = products.filter(Q(module_komplekt=u'Комплект'))
    elif type == 'modules':
        products = products.filter(Q(module_komplekt=u'Модуль'))
    elif type == 'others':
        products = products.filter(Q(module_komplekt__isnull=True))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_children_rooms(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель') & Q(room=u'Детские'))
    if type == 'komplekts':
        products = products.filter(Q(module_komplekt=u'Комплект'))
    elif type == 'modules':
        products = products.filter(Q(module_komplekt=u'Модуль'))
    elif type == 'others':
        products = products.filter(Q(module_komplekt__isnull=True))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_tv_tumbs(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель') & Q(module_mebel=u'ТВ-тумба'))
    if type == 'komplekts':
        products = products.filter(Q(module_komplekt=u'Комплект'))
    elif type == 'modules':
        products = products.filter(Q(module_komplekt=u'Модуль'))
    elif type == 'others':
        products = products.filter(Q(module_komplekt__isnull=True))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_other_furniture(request, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel__isnull=True) & Q(room__isnull=True))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_cases(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель'))
    if type == 'doors_1':
        products = products.filter(Q(doors=1))
    elif type == 'doors_2':
        products = products.filter(Q(doors=2))
    elif type == 'doors_3':
        products = products.filter(Q(doors=3))
    elif type == 'doors_4':
        products = products.filter(Q(doors=4))
    elif type == 'doors_5':
        products = products.filter(Q(doors=5))
    elif type == 'doors_6':
        products = products.filter(Q(doors=6))
    elif type == 'cases_corners':
        products = products.filter(Q(shape=u'Угловой'))
    elif type == 'cases_others':
        products = products.filter(Q(doors__gte=6))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def carcass_furniture_beds(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Корпусная мебель'))
    if type == 'length_80':
        products = products.filter(Q(length=80))
    elif type == 'length_90':
        products = products.filter(Q(length=90))
    elif type == 'length_120':
        products = products.filter(Q(length=120))
    elif type == 'length_140':
        products = products.filter(Q(length=140))
    elif type == 'length_160':
        products = products.filter(Q(length=160))
    elif type == 'length_180':
        products = products.filter(Q(length=180))
    elif type == 'cases_corners':
        products = products.filter(Q(architecture_type=u'Двухъярусная кровать'))
    elif type == 'cases_others':
        products = products.filter(Q(length__gte=180))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def cushioned_furniture_komplekts(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Мягкая мебель') & Q(module_komplekt=u'Комплект'))
    if type == 'd_2kr_kr':
        products = products.filter(Q(soft_komplekt=u'Диван + 2 кресла-кровати'))
    elif type == 'd_2kr_kr_kr':
        products = products.filter(Q(soft_komplekt=u'Диван + 2 кресла + кресло-кровать'))
    elif type == 'd_kr_2kr_kr':
        products = products.filter(Q(soft_komplekt=u'Диван-кровать + 2 кресла-кровати'))
    elif type == 'glkr_2glkr':
        products = products.filter(Q(soft_komplekt=u'Глухой диван + 2 глухих кресла'))
    elif type == 'ugd_glkr':
        products = products.filter(Q(soft_komplekt=u'Угловой диван + глухое кресло'))
    elif type == 'ugd_krkr':
        products = products.filter(Q(soft_komplekt=u'Угловой диван + кресло-кровать'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def cushioned_furniture_corners(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Мягкая мебель') & Q(shape=u'Угловые'))
    if type == 'rollable':
        products = products.filter(Q(architecture_type=u'Выкатные'))
    elif type == 'classic':
        products = products.filter(Q(architecture_type=u'Классические'))
    elif type == 'metalkarkas':
        products = products.filter(Q(materal=u'Металлокаркас'))
    elif type == 'euro':
        products = products.filter(Q(architecture_type=u'Евро'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def cushioned_furniture_sofas(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Мягкая мебель') & Q(module_mebel=u'Диван'))
    if type == 'classic':
        products = products.filter(Q(architecture_type=u'Классические'))
    elif type == 'euro_book':
        products = products.filter(Q(architecture_type=u'Евро-книжка'))
    elif type == 'book':
        products = products.filter(Q(architecture_type=u'Книжка'))
    elif type == 'rollable':
        products = products.filter(Q(architecture_type=u'Выкатные'))
    elif type == 'metalkarkas':
        products = products.filter(Q(architecture_type=u'Металлокаркас') | Q(materal=u'Металлокаркас'))
    elif type == 'mini':
        products = products.filter(Q(architecture_type=u'Мини'))
    elif type == 'office':
        products = products.filter(Q(architecture_type=u'Офисные') | Q(style=u'Офисные'))
    elif type == 'rotang':
        products = products.filter(Q(materal__icontains=u'Ротанг'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def cushioned_furniture_armchairs(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Мягкая мебель') & Q(module_mebel=u'Кресло'))
    if type == 'classic':
        products = products.filter(Q(architecture_type=u'Классические'))
    elif type == 'euro_book':
        products = products.filter(Q(architecture_type=u'Евро-книжка'))
    elif type == 'book':
        products = products.filter(Q(architecture_type=u'Книжка'))
    elif type == 'rollable':
        products = products.filter(Q(architecture_type=u'Выкатные'))
    elif type == 'metalkarkas':
        products = products.filter(Q(architecture_type=u'Металлокаркас') | Q(materal=u'Металлокаркас'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def cushioned_furniture_on_orders(request, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Мягкая мебель') & Q(on_order=True))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def office_furniture_sofas(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Мягкая мебель') & Q(module_mebel=u'Диван'))
    if type == 'strait':
        products = products.filter(Q(shape=u'Прямые'))
    elif type == 'corner':
        products = products.filter(Q(shape=u'Угловые'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def office_furniture_tables(request, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Мягкая мебель') & Q(module_mebel=u'Стол'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def office_furniture_cases(request, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Мягкая мебель') & Q(module_mebel=u'Шкаф'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def office_furniture_libraries(request, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Мягкая мебель') & Q(module_mebel=u'Библиотека'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def office_furniture_armchairs(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Мягкая мебель') & Q(module_mebel=u'Кресло'))
    if type == 'chief':
        products = products.filter(Q(armchaire_role=u'Для руководителя'))
    elif type == 'personel':
        products = products.filter(Q(armchaire_role=u'Для персонала'))
    elif type == 'managers':
        products = products.filter(Q(armchaire_role=u'Для менеджеров'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def office_furniture_divider(request, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Мягкая мебель'))
    products = Product.active.filter(Q(module_mebel=u'Ресепшн') | Q(module_mebel=u'Перегородка'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def fireplace_kamin_komplekt(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Каминный комплект'))
    if type == 'vigodnie':
        products = products.filter(Q(is_featured=True))
    elif type == 'stone':
        products = products.filter(Q(brand=u'Stone'))
    elif type == 'new_look':
        products = products.filter(Q(brand=u'New Look'))
    elif type == 'mini':
        products = products.filter(Q(brand=u'Mini'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def fireplace_serii(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(komplekt_mebel=u'Каминный комплект'))
    if type == 'castle':
        products = products.filter(Q(brand=u'Castle'))
    elif type == 'stone':
        products = products.filter(Q(brand=u'Stone'))
    elif type == 'classic':
        products = products.filter(Q(brand=u'Classic'))
    elif type == 'new_look':
        products = products.filter(Q(brand=u'New Look'))
    elif type == 'mini':
        products = products.filter(Q(brand=u'Mini'))
    elif type == 'marble':
        products = products.filter(Q(brand=u'Marble'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def fireplace_portals(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_other=u'Камин-портал'))
    if type == 'natural_marble':
        products = products.filter(Q(materal=u'Натуральный мрамор'))
    elif type == 'polimer_stone':
        products = products.filter(Q(materal=u'Полимерный камень'))
    elif type == 'mdf':
        products = products.filter(Q(materal=u'МДФ'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def fireplace_electrokamins(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_other=u'Камин-электрокамин'))
    if type == 'wide_flame':
        products = products.filter(Q(ochag=u'Широкий очаг'))
    elif type == 'standard_flame':
        products = products.filter(Q(ochag=u'Стандартный очаг'))
    elif type == 'hover_flame':
        products = products.filter(Q(ochag=u'Навесной очаг'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def fireplace_ovens(request, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_other=u'Камин-печь'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def fireplace_accesories(request, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_other=u'Камин-аксессуар'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def tables_foldable(request, type1, type2, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_mebel=u'Стол'))
    products = products.filter(Q(architecture_type=u'Раскладные'))
    if type1 == 'wooden':
        products = products.filter(Q(materal=u'Деревянные'))
    elif type1 == 'glass':
        products = products.filter(Q(materal=u'Стеклянные'))
    elif type1 == 'ldsp':
        products = products.filter(Q(materal=u'ЛДСП'))
    elif type1 == 'others':
        products = products.filter(~Q(materal=u'Деревянные') & ~Q(materal=u'Стеклянные') & ~Q(materal=u'ЛДСП'))
    if type2 == 'round':
        products = products.filter(Q(shape=u'Круглые'))
    elif type2 == 'oval':
        products = products.filter(Q(shape=u'Овальные'))
    elif type2 == 'rectangle':
        products = products.filter(Q(shape=u'Прямоугольные'))
    elif type2 == 'others':
        products = products.filter(~Q(shape=u'Круглые') & ~Q(shape=u'Овальные') & ~Q(shape=u'Прямоугольные'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def tables_unfoldable(request, type1, type2, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_mebel=u'Стол'))
    products = products.filter(~Q(architecture_type=u'Раскладные'))
    if type1 == 'wooden':
        products = products.filter(Q(materal=u'Деревянные'))
    elif type1 == 'glass':
        products = products.filter(Q(materal=u'Стеклянные'))
    elif type1 == 'ldsp':
        products = products.filter(Q(materal=u'ЛДСП'))
    elif type1 == 'others':
        products = products.filter(~Q(materal=u'Деревянные') & ~Q(materal=u'Стеклянные') & ~Q(materal=u'ЛДСП'))
    if type2 == 'round':
        products = products.filter(Q(shape=u'Круглые'))
    elif type2 == 'oval':
        products = products.filter(Q(shape=u'Овальные'))
    elif type2 == 'rectangle':
        products = products.filter(Q(shape=u'Прямоугольные'))
    elif type2 == 'others':
        products = products.filter(~Q(shape=u'Круглые') & ~Q(shape=u'Овальные') & ~Q(shape=u'Прямоугольные'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def chairs_wooden(request, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_mebel=u'Стул'))
    products = products.filter(Q(material=u'Деревянные'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def chairs_metalkarkas(request, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_mebel=u'Стул'))
    products = products.filter(Q(material=u'Металлокаркас'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def chairs_plastic(request, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_mebel=u'Стул'))
    products = products.filter(Q(material=u'Пластиковые'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def chairs_barniy(request, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_mebel=u'Стул'))
    products = products.filter(Q(style=u'Для баров и ресторанов'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def chairs_foldable(request, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_mebel=u'Стул'))
    products = products.filter(Q(architecture_type=u'Раскладные'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def chairs_others(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_mebel=u'Стул'))
    if type == 'rotang':
        products = products.filter(Q(rotang=True))
    elif type == 'office':
        products = products.filter(Q(architecture_type=u'Офисные') | Q(style=u'Офисные'))
    elif type == 'cinema':
        products = products.filter(Q(style=u'Для кинотеатров'))
    elif type == 'visitors':
        products = products.filter(Q(style=u'Для посетителей'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def kitchen_corners_komplekts(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_komplekt=u'Комплект'))
    products = products.filter(Q(shape=u'Угловые'))
    products = products.filter(Q(room=u'Кухня'))
    if type == 'wooden':
        products = products.filter(Q(material=u'Деревянные'))
    elif type == 'ldsp':
        products = products.filter(Q(material=u'ЛДСП'))
    elif type == 'metalkarkas':
        products = products.filter(Q(material=u'Металлокаркас'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def kitchen_corners_module(request, type1, type2, template_name="catalog/category.html"):
    products = Product.active.filter(Q(peace_of__isnull=False))
    products = products.filter(Q(room=u'Кухня'))
    if type1 == 'wooden':
        products = products.filter(Q(materal=u'Деревянные'))
    elif type1 == 'ldsp':
        products = products.filter(Q(materal=u'ЛДСП'))
    elif type1 == 'metalkarkas':
        products = products.filter(Q(materal=u'Металлокаркас'))
    if type2 == 'tables':
        products = products.filter(Q(module_mebel=u'Стол'))
    elif type2 == 'chairs':
        products = products.filter(Q(module_mebel=u'Стул'))
    elif type2 == 'corners':
        products = products.filter(Q(module_mebel=u'Кухонный уголок'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def kitchen_corner_sofa(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_mebel=u'Диван'))
    products = products.filter(Q(room=u'Кухня'))
    products = products.filter(Q(shape=u'Угловые'))
    if type == 'foldable':
        products = products.filter(Q(architecture_type=u'Раскладные'))
    elif type == 'unfoldable':
        products = products.filter(~Q(architecture_type=u'Раскладные'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def kitchen_corner_from(request, template_name="catalog/category.html"):
    products = Product.active.filter(Q(shape=u'Угловые'))
    products = products.filter(Q(room=u'Кухня'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def matrasses(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_mebel=u'Матрас'))
    if type == 'springing':
        products = products.filter(Q(architecture_type=u'Пружинные'))
    elif type == 'ortoped':
        products = products.filter(~Q(architecture_type=u'Ортопедические'))
    elif type == 'anatom':
        products = products.filter(~Q(architecture_type=u'Анатомические'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def garden_furniture_rotang(request, type1, type2, type3, template_name="catalog/category.html"):
    products = Product.active.filter(Q(style=u'Садовые'))
    products = products.filter(Q(rotang=True))
    if type1 == 'artificial':
        products = products.filter(Q(materal=u'Ротанг искусственный'))
    elif type1 == 'natural':
        products = products.filter(Q(materal=u'Ротанг натуральный'))
    elif type1 == 'wooden':
        products = products.filter(Q(materal=u'Деревянные'))
    if type2 == 'sofas':
        products = products.filter(Q(module_mebel=u'Диван'))
    elif type2 == 'tables':
        products = products.filter(Q(module_mebel=u'Стол'))
    elif type2 == 'armchairs':
        products = products.filter(Q(module_mebel=u'Кресло'))
    elif type2 == 'chairs':
        products = products.filter(Q(module_mebel=u'Стул'))
    if type3 == 'mini':
        products = products.filter(Q(architecture_type=u'Мини'))
    elif type3 == 'standard':
        products = products.filter(Q(architecture_type=u'Стандарт'))
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

def bars_restaurants(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(style=u'Для баров и ресторанов'))
    if type == 'tables':
        products = products.filter(Q(module_mebel=u'Стол'))
    elif type == 'chairs':
        products = products.filter(~Q(module_mebel=u'Стул'))
    elif type == 'sofas':
        products = products.filter(~Q(module_mebel=u'Диван'))
    elif type == 'vintage':
        products = products.filter(~Q(style=u'Под старину'))
    elif type == 'stoyki':
        products = products.filter(~Q(module_mebel=u'Прилавок'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def case_kupe(request, template_name="catalog/category.html"):
    products = Product.active.filter(Q(architecture_type=u'Шкаф-купе'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def hotels(request, template_name="catalog/category.html"):
    products = Product.active.filter(Q(style=u'Гостиничные номера'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def interier(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_komplekt=u'Интерьер'))
    if type == 'flowers':
        products = products.filter(Q(module_other=u'Цветы'))
    elif type == 'statues':
        products = products.filter(~Q(module_other=u'Статуэтка'))
    elif type == 'pictures':
        products = products.filter(~Q(module_other=u'Картина'))
    elif type == 'buckets':
        products = products.filter(~Q(module_other=u'Сундук'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def interier_vases(request, type, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_komplekt=u'Интерьер'))
    products = products.filter(Q(module_other=u'Ваза'))
    if type == 'glass':
        products = products.filter(Q(module_other=u'Стеклянные'))
    elif type == 'pletenie':
        products = products.filter(Q(module_other=u'Плетеные'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def others(request, template_name="catalog/category.html"):
    products = Product.active.filter(Q(module_other=u'Разное'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def associated_goods(request, type, template_name="catalog/category.html"):
    products = Product.active.all()
    if type == 'electronics':
        products = products.filter(Q(module_other=u'Электротовар'))
    elif type == 'smesitels':
        products = products.filter(~Q(module_other=u'Смеситель'))
    elif type == 'stoves':
        products = products.filter(~Q(module_other=u'Плита'))
    elif type == 'refrigirators':
        products = products.filter(~Q(module_other=u'Холодильник'))
    elif type == 'sinks':
        products = products.filter(~Q(module_other=u'Мойка'))
    elif type == 'aprons':
        products = products.filter(~Q(module_other=u'Фартук'))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def individual_orders(request, template_name="catalog/category.html"):
    products = Product.active.filter(Q(on_order=True))
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

# def show_category(request, category_slug, gender='', template_name="catalog/category.html"):
#     c = get_object_or_404(Category, slug=category_slug)
#     gender = gender.upper()
#     products = c.product_set.all()
#     if gender:
#         products = products.filter(Q(gender = gender) | Q(gender = 'UNI'))
#     page_title = c.name
#     meta_keywords = c.meta_keywords
#     meta_description = c.meta_description
#     return render_to_response(template_name, locals(), context_instance=RequestContext(request))


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
    else:
        # its a GET,create the unbound form. Note request as a kwarg
        form = ProductAddToCartForm(request=request, label_suffix=':')
        # assign the hidden input the product slug
    form.fields['product_slug'].widget.attrs['value'] = product_slug
    # set the test cookie on our first GET request
    request.session.set_test_cookie()
    stats.log_product_view(request, p)  # add to product view
    product_reviews = ProductReview.approved.filter(product=p).order_by('-date')
    review_form = ProductReviewForm()
    return render_to_response("catalog/product.html", locals(), context_instance=RequestContext(request))


@login_required
def add_review(request):
    form = ProductReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        slug = request.POST.get('slug')
        product = Product.active.get(slug=slug)
        review.user = request.user
        review.product = product
        review.save()
        template = "catalog/product_review.html"
        html = render_to_string(template, {'review': review})
        response = json.dumps({'success': 'True', 'html': html})
    else:
        html = form.errors.as_ul()
        response = json.dumps({'success': 'False', 'html': html})
    return HttpResponse(response, content_type='application/javascript; charset=utf-8')
