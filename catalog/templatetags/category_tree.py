# -*- coding: utf-8 -*-

# Каталог
main_tree = (
    (u'Корпусная мебель', 'carcass-furniture'),
    (u'Мягкая мебель', 'cushioned-furniture'),
    (u'Офисная мебель', 'office-furniture'),
    (u'Камины', 'fireplace'),
    (u'Столы', 'tables'),
    (u'Стулья', 'chairs'),
    (u'Кухонные уголки', 'kitchen-corners'),
    (u'Матрасы', 'matrasses'),
    (u'Садовая мебель', 'garden-furniture'),
    (u'Шкафы-купе', 'case-kupe'),
    (u'Гостиничные номера', 'hotels'),
    (u'Интерьер', 'interier'),
    (u'Разное', 'others'),
    (u'Сопутствующие товары', 'associated-goods'),
    (u'Индивидуальные заказы', 'individual-orders'),
)

# Корпусная мебель
carcass_furniture = (
    (u'Кухни', 'kitchens'),
    (u'Горки, стенки, гостинные', 'gorki-stenki-gestrooms'),
    (u'Спальни', 'bedrooms'),
    (u'Прихожие', 'corridors'),
    (u'Детские', 'children-rooms'),
    (u'Другая мебель', 'other-furniture'),
    (u'Шкафы', 'cases'),
    (u'Кровати', 'beds'),
    (u'ТВ-тумбы', 'tv-tumbs'),
)

carcass_furniture_level2 = (
    (u'Комплекты', 'komplekts'),
    (u'Модульно', 'modules'),
    # (u'Сопутствующие товары', 'associated-goods'),
    # (u'Библиотеки', 'libraries'),
    (u'Другое', 'others'),
)

associated_goods = (
    (u'Электротовары', 'electronics'),
    (u'Смесители', 'smesitels'),
    (u'Плиты', 'stoves'),
    (u'Холодильники', 'refrigirators'),
    (u'Мойки', 'sinks'),
    (u'Фартуки', 'aprons'),
)

cases = (
    (u'1-х дверные', 'doors-1'),
    (u'2-х дверные', 'doors-2'),
    (u'3-х дверные', 'doors-3'),
    (u'4-х дверные', 'doors-4'),
    (u'5-х дверные', 'doors-5'),
    (u'6-х дверные', 'doors-6'),
    (u'Угловые', 'cases-corners'),
    (u'Другое', 'cases-others'),
)

beds = (
    (u'80 см', 'length-80'),
    (u'90 см', 'length-90'),
    (u'120 см', 'length-120'),
    (u'140 см', 'length-140'),
    (u'160 см', 'length-160'),
    (u'180 см', 'length-180'),
    (u'Другое', 'beds-others'),
    (u'Двухъярусные', 'beds-double'),
)
# КОНЕЦ корпусная мебель


# Мягкая мебель
cushioned_furniture = (
    (u'Комплекты', 'cushioned-komplekts'),
    (u'Угловые', 'cushioned-corners'),
    (u'Диваны', 'cushioned-sofas'),
    (u'Кресла', 'cushioned-armchairs'),
    (u'Под заказ', 'cushioned-on-orders'),
)

# Комплекты
cushioned_furniture_komplekts = (
    (u'Диван + 2 кресла-кровати', 'd-2kr-kr'),
    (u'Диван + 2 кресла + кресло-кровать', 'd-2kr-kr-kr'),
    (u'Диван-кровать + 2 кресла-кровати', 'd-kr-2kr-kr'),
    (u'Глухой диван + 2 глухих кресла', 'glkr-2glkr'),
    (u'Угловой диван + глухое кресло', 'ugd-glkr'),
    (u'Угловой диван + кресло-кровать', 'ugd-krkr'),
)

# Угловые
cushioned_furniture_corners = (
    (u'Выкатные','cushioned-rollable'),
    (u'Классические','cushioned-classic'),
    (u'Металлокарскас','cushioned-metalkarkas'),
    (u'Евро','cushioned-euro'),
)

# Диваны
cushioned_furniture_sofas = (
    (u'Классические','cushioned-classic'),
    (u'Евро-книжка','cushioned-euro-book'),
    (u'Книжка','cushioned-book'),
    (u'Выкатной','cushioned-rollable'),
    (u'Металлокаркас','cushioned-metalkarkas'),
    (u'Мини','cushioned-mini'),
    (u'Офисный','cushioned-office'),
    (u'Ротанг','cushioned-rotang'),
)

# Кресла
cushioned_furniture_armchairs = (
    (u'Кресла','cushioned-classic'),
    (u'Кресла-кровати','cushioned-euro-book'),
    (u'Кресла-качалки','cushioned-book'),
    (u'Офисные кресла','cushioned-rollable'),
    (u'Банкетки','cushioned-metalkarkas'),
)

# КОНЕЦ мягкая мебель ####

# Офисная мебель
office_furniture = (
    (u'Диваны', 'sofas'),
    (u'Столы', 'tables'),
    (u'Шкафы', 'cases'),
    (u'Библиотеки', 'libraries'),
    (u'Кресла', 'armchairs'),
    (u'Стулья', 'chairs'),
    (u'Перегородки', 'divider'),
)

# Камины
fireplaces = (
    (u'Каминные комплекты', 'kamin-komplekt'),
    (u'Серии', 'serii'),
    (u'Порталы', 'portals'),
    (u'Электрокамины', 'electrokamins'),
    (u'Печи', 'ovens'),
    (u'Аксессуары', 'accesories'),
)

# Столы
tables = (
    (u'Раскладные', 'foldable-table'),
    (u'Нераскладные', 'unfoldable-table'),
)

# Стулья
chairs = (
    (u'Деревянные', 'wooden'),
    (u'Металлокаркас', 'metalkarkas'),
    (u'Пластиковые', 'plastic'),
    (u'Разные', 'others'),
    (u'Барные', 'barniy'),
    (u'Складные', 'foldable'),
)

# Кухонные уголки
kitchen_corners = (
    (u'Комплекты', 'komplekts'),
    (u'Модульно', 'module'),
    (u'Кухонные+угловые диваны', 'kitchen-corner-sofa'),
    (u'Уголки от', 'corners-from'),
)

# Матрасы
matrasses = (
    (u'Пружинные', 'springing'),
    (u'Ортопедические', 'ortoped'),
    (u'Анатомические', 'anatom'),
)

# Садовая мебель
garden_furniture = (
    (u'Ротанг', 'rotang'),
    (u'Качели', 'kacheli'),
    (u'Раскладушки', 'foldable'),
    (u'Кресла', 'armchair'),
    (u'Шезлонги', 'shezlong'),
    (u'Другое', 'others'),
)

# Для баров и ресторанов
bars_restaurants = (
    (u'Столы', 'tables'),
    (u'Стулы', 'chairs'),
    (u'Диваны', 'sofas'),
    (u'Под старину', 'vintage'),
    (u'Стойки', 'stoyki'),
)

# Интерьер
interier = (
    (u'Цветы', 'flowers'),
    (u'Статуэтки', 'statues'),
    (u'Картины', 'pictures'),
    (u'Вазы', 'vases'),
    (u'Корзины', 'buckets'),
)