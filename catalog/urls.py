from django.conf.urls import url, include
from views import *


carcass_furniture = [
    url(r'kitchens/(?P<type>[-_\w]+)$', carcass_furniture_kitchens, name='carcass_furniture_kitchens'),
    url(r'gorki_stenki_gestrooms/(?P<type>[-_\w]+)$', carcass_furniture_gorki_stenki_gestrooms, name='carcass_furniture_gorki_stenki_gestrooms'),
    url(r'bedrooms/(?P<type>[-_\w]+)$', carcass_furniture_bedrooms, name='carcass_furniture_bedrooms'),
    url(r'corridors/(?P<type>[-_\w]+)$', carcass_furniture_corridors, name='carcass_furniture_corridors'),
    url(r'children_rooms/(?P<type>[-_\w]+)$', carcass_furniture_children_rooms, name='carcass_furniture_children_rooms'),
    url(r'other_furniture$', carcass_furniture_other_furniture, name='carcass_furniture_other_furniture'),
    url(r'cases/(?P<type>[-_\w]+)$', carcass_furniture_cases, name='carcass_furniture_cases'),
    url(r'beds/(?P<type>[-_\w]+)$', carcass_furniture_beds, name='carcass_furniture_beds'),
    url(r'tv_tumbs/(?P<type>[-_\w]+)$', carcass_furniture_tv_tumbs, name='carcass_furniture_tv_tumbs'),
]


cushioned_furniture = [
    url(r'komplekts/(?P<type>[-_\w]+)$', cushioned_furniture_komplekts, name='cushioned_furniture_komplekts'),
    url(r'corners/(?P<type>[-_\w]+)$', cushioned_furniture_corners, name='cushioned_furniture_corners'),
    url(r'sofas/(?P<type>[-_\w]+)$', cushioned_furniture_sofas, name='cushioned_furniture_sofas'),
    url(r'armchairs/(?P<type>[-_\w]+)$', cushioned_furniture_armchairs, name='cushioned_furniture_armchairs'),
    url(r'on_order$', cushioned_furniture_on_orders, name='cushioned_furniture_on_orders'),
]

office_furniture = [
    url(r'sofas/(?P<type>[-_\w]+)$', office_furniture_sofas, name='office_furniture_sofas'),
    url(r'tables$', office_furniture_tables, name='office_furniture_tables'),
    url(r'cases$', office_furniture_cases, name='office_furniture_cases'),
    url(r'libraries$', office_furniture_libraries, name='office_furniture_libraries'),
    url(r'armchairs/(?P<type>[-_\w]+)$', office_furniture_armchairs, name='office_furniture_armchairs'),
    url(r'divider/reseption$', office_furniture_divider, name='office_furniture_divider'),
]

fireplace = [
    url(r'kamin_komplekt/(?P<type>[-_\w]+)$', fireplace_kamin_komplekt, name='fireplace_kamin_komplekt'),
    url(r'serii/(?P<type>[-_\w]+)$', fireplace_serii, name='fireplace_serii'),
    url(r'portals/(?P<type>[-_\w]+)$', fireplace_portals, name='fireplace_portals'),
    url(r'electrokamins/(?P<type>[-_\w]+)$', fireplace_electrokamins, name='fireplace_electrokamins'),
    url(r'ovens$', fireplace_ovens, name='fireplace_ovens'),
    url(r'accesories$', fireplace_accesories, name='fireplace_accesories'),
]

tables = [
    url(r'foldable/(?P<type1>[-_\w]+)/(?P<type2>[-_\w]+)$', tables_foldable, name='tables_foldable'),
    url(r'unfoldable/(?P<type1>[-_\w]+)/(?P<type2>[-_\w]+)$', tables_unfoldable, name='tables_unfoldable'),
]

chairs = [
    url(r'wooden$', chairs_wooden, name='chairs_wooden'),
    url(r'metalkarkas$', chairs_metalkarkas, name='chairs_metalkarkas'),
    url(r'plastic$', chairs_plastic, name='chairs_plastic'),
    url(r'others/(?P<type>[-_\w]+)$', chairs_others, name='chairs_others'),
    url(r'barniy$', chairs_barniy, name='chairs_barniy'),
    url(r'foldable$', chairs_foldable, name='chairs_foldable'),
]

kitchen_corners = [
    url(r'komplekts/(?P<type>[-_\w]+)$', kitchen_corners_komplekts, name='kitchen_corners_komplekts'),
    url(r'module/(?P<type1>[-_\w]+)/(?P<type2>[-_\w]+)$', kitchen_corners_module, name='kitchen_corners_module'),
    url(r'kitchen_corner_sofa/(?P<type>[-_\w]+)$', kitchen_corner_sofa, name='kitchen_corner_sofa'),
    url(r'corners_from$', kitchen_corner_from, name='kitchen_corner_from'),
]

matrasses = [
    url(r'(?P<type>[-_\w]+)$', matrasses, name='matrasses'),
]

garden_furniture = [
    url(r'rotang/(?P<type1>[-_\w]+)/(?P<type2>[-_\w]+)/(?P<type3>[-_\w]+)$', garden_furniture_rotang, name='garden_furniture_rotang'),
    url(r'kacheli$', garden_furniture_kacheli, name='garden_furniture_kacheli'),
    url(r'raskladushka$', garden_furniture_raskladushka, name='garden_furniture_raskladushka'),
    url(r'armchairs$', garden_furniture_armchair, name='garden_furniture_armchair'),
    url(r'shezlong$', garden_furniture_shezlong, name='garden_furniture_shezlong'),
    url(r'others$', garden_furniture_others, name='garden_furniture_others'),
]

bars_restaurants = [
    url(r'(?P<type>[-_\w]+)', bars_restaurants, name='bars_restaurants'),
]

case_kupe = [
    url(r'$', case_kupe, name='case_kupe'),
]

hotels = [
    url(r'$', hotels, name='hotels'),
]

interier = [
    url(r'(?P<type>[-_\w]+)', interier, name='interier'),
    url(r'vases/(?P<type>[-_\w]+)$', interier_vases, name='interier_vases'),
]

others = [
    url(r'$', others, name='others'),
]

associated_goods = [
    url(r'^(?P<type>[-_\w]+)$', associated_goods, name='associated_goods'),
]

individual_orders = [
    url(r'^$', individual_orders, name='individual_orders'),
]


urlpatterns = [
    url(r'^$', index, {'template_name': 'catalog/index.html'}, 'catalog_home'),
    url(r'^about$', about, {'template_name': 'flatpages/about.html'}, 'about'),
    url(r'^contact$', contact, {'template_name': 'flatpages/contact.html'}, 'contact'),
    url(r'^delivery$', delivery, {'template_name': 'flatpages/delivery.html'}, 'delivery'),
    url(r'^faq', faq, {'template_name': 'flatpages/faq.html'}, 'faq'),
    url(r'^product/(?P<product_slug>[-\w]+)/$', show_product, {'template_name': 'catalog/product.html'},
        'catalog_product'),
    url(r'carcass_furniture/', include(carcass_furniture)),
    url(r'cushioned_furniture/', include(cushioned_furniture)),
    url(r'office_furniture/', include(office_furniture)),
    url(r'fireplace/', include(fireplace)),
    url(r'tables/', include(tables)),
    url(r'chairs/', include(chairs)),
    url(r'kitchen_corners/', include(kitchen_corners)),
    url(r'matrasses/', include(matrasses)),
    url(r'garden_furniture/', include(garden_furniture)),
    url(r'bars_restaurants/', include(bars_restaurants)),
    url(r'case_kupe/', include(case_kupe)),
    url(r'hotels/', include(hotels)),
    url(r'interier/', include(interier)),
    url(r'others/', include(others)),
    url(r'associated_goods/', include(associated_goods)),
    url(r'individual_orders/', include(individual_orders)),
]