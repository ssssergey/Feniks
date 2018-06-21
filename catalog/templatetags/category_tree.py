# _*_ coding: utf_8 _*_

# Каталог
main_tree = (
    (u'Корпусная мебель', 'carcass_furniture'),
    (u'Мягкая мебель', 'cushioned_furniture'),
    (u'Офисная мебель', 'office_furniture'),
    (u'Камины', 'fireplace'),
    (u'Столы', 'tables'),
    (u'Стулья', 'chairs'),
    (u'Кухонные уголки', 'kitchen_corners'),
    (u'Матрасы', 'matrasses'),
    (u'Садовая мебель', 'garden_furniture'),
    (u'Для баров и ресторанов', 'bars_restaurants'),
    (u'Шкафы-купе', 'case_kupe'),
    (u'Гостиничные номера', 'hotels'),
    (u'Интерьер', 'interier'),
    (u'Разное', 'others'),
    (u'Сопутствующие товары', 'associated_goods'),
    (u'Индивидуальные заказы', 'individual_orders'),
)

# Корпусная мебель
carcass_furniture = (
    (u'Кухни', 'kitchens'),
    (u'Горки, стенки, гостинные', 'gorki_stenki_gestrooms'),
    (u'Спальни', 'bedrooms'),
    (u'Прихожие', 'corridors'),
    (u'Детские', 'children_rooms'),
    (u'Другая мебель', 'other_furniture'),
    (u'Шкафы', 'cases'),
    (u'Кровати', 'beds'),
    (u'ТВ-тумбы', 'tv_tumbs'),
)

carcass_furniture_level2 = (
    (u'Комплекты', 'komplekts'),
    (u'Модульно', 'modules'),
    # (u'Сопутствующие товары', 'associated_goods'),
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
    (u'1_х дверные', 'doors_1'),
    (u'2_х дверные', 'doors_2'),
    (u'3_х дверные', 'doors_3'),
    (u'4_х дверные', 'doors_4'),
    (u'5_х дверные', 'doors_5'),
    (u'6_х дверные', 'doors_6'),
    (u'Угловые', 'cases_corners'),
    (u'Другое', 'cases_others'),
)

beds = (
    (u'80 см', 'length_80'),
    (u'90 см', 'length_90'),
    (u'120 см', 'length_120'),
    (u'140 см', 'length_140'),
    (u'160 см', 'length_160'),
    (u'180 см', 'length_180'),
    (u'Другое', 'others'),
    (u'Двухъярусные', 'double'),
)
# КОНЕЦ корпусная мебель


# Мягкая мебель
cushioned_furniture = (
    (u'Комплекты', 'komplekts'),
    (u'Угловые', 'corners'),
    (u'Диваны', 'sofas'),
    (u'Кресла', 'armchairs'),
    (u'Под заказ', 'on_order'),
)

# Комплекты
cushioned_furniture_komplekts = (
    (u'Диван + 2 кресла_кровати', 'd_2kr_kr'),
    (u'Диван + 2 кресла + кресло_кровать', 'd_2kr_kr_kr'),
    (u'Диван-кровать + 2 кресла-кровати', 'd_kr_2kr_kr'),
    (u'Глухой диван + 2 глухих кресла', 'glkr_2glkr'),
    (u'Угловой диван + глухое кресло', 'ugd_glkr'),
    (u'Угловой диван + кресло-кровать', 'ugd_krkr'),
)

# Угловые
cushioned_furniture_corners = (
    (u'Выкатные', 'rollable'),
    (u'Классические', 'classic'),
    (u'Металлокарскас', 'metalkarkas'),
    (u'Евро', 'euro'),
)

# Диваны
cushioned_furniture_sofas = (
    (u'Классические', 'classic'),
    (u'Евро-книжка', 'euro_book'),
    (u'Книжка', 'book'),
    (u'Выкатной', 'rollable'),
    (u'Металлокаркас', 'metalkarkas'),
    (u'Мини', 'mini'),
    (u'Офисный', 'office'),
    (u'Ротанг', 'rotang')
)

# Кресла
cushioned_furniture_armchairs = (
    (u'Кресла', 'classic'),
    (u'Кресла-кровати', 'euro_book'),
    (u'Кресла-качалки', 'book'),
    (u'Офисные кресла', 'rollable'),
    (u'Банкетки', 'metalkarkas')
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
    (u'Каминные комплекты', 'kamin_komplekt'),
    (u'Серии', 'serii'),
    (u'Порталы', 'portals'),
    (u'Электрокамины', 'electrokamins'),
    (u'Печи', 'ovens'),
    (u'Аксессуары', 'accesories'),
)

kamin_komplekti = (
    (u'Выгодные', 'vigodnie'),
    (u'Stone', 'stone'),
    (u'New Look', 'new_look'),
    (u'Mini', 'mini'),
)

serii = (
    (u'Castle', 'castle'),
    (u'Stone', 'stone'),
    (u'Classic', 'classic'),
    (u'New Look', 'new_look'),
    (u'Mini', 'mini'),
    (u'Marble', 'marble'),
)

portals = (
    (u'Натуральный мрамор', 'natural_marble'),
    (u'Полимерный камень', 'polimer_stone'),
    (u'МДФ+', 'mdf'),
)

electrokamins = (
    (u'Широкие очаги', 'wide_flame'),
    (u'Стандартные очаги', 'standard_flame'),
    (u'Навесные очаги', 'hover_flame'),
)

# Столы
tables = (
    (u'Раскладные', 'foldable'),
    (u'Нераскладные', 'unfoldable'),
)

tables_level2 = (
    (u'Деревянные', 'wooden'),
    (u'Стекло', 'glass'),
    (u'ЛДСП', 'ldsp'),
    (u'Другие', 'others'),
)

tables_level3 = (
    (u'Круглые', 'round'),
    (u'Овальные', 'oval'),
    (u'Прямоугольные', 'rectangle'),
    (u'Другие', 'others'),
)

tables_others = (
    (u'Офисные', 'office'),
    (u'Ротанг', 'rotang'),
    (u'Садовые', 'garden'),
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

chairs_others = (
    (u'Ротанг', 'rotang'),
    (u'Офисные', 'office'),
    (u'Для кинотеатров', 'cinema'),
    (u'Для посетителей', 'visitors'),
)

# Кухонные уголки
kitchen_corners = (
    (u'Комплекты', 'komplekts'),
    (u'Модульно', 'module'),
    (u'Кухонные+угловые диваны', 'kitchen_corner_sofa'),
    (u'Уголки от', 'corners_from'),
)

kitchen_corners_level2 = (
    (u'Дерево', 'wooden'),
    (u'ЛДСП', 'ldsp'),
    (u'Металлокаркас', 'metalkarkas'),
)

kitchen_corners_level3 = (
    (u'Столы', 'tables'),
    (u'Стулья', 'chairs'),
    (u'Уголки', 'corners'),
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
    (u'Кресла', 'armchairs'),
    (u'Шезлонги', 'shezlong'),
    (u'Другое', 'others'),
)

rotang = (
    (u'Искусственный', 'artificial'),
    (u'Натуральный', 'natural'),
    (u'Дерево', 'wooden'),
)

rotang_level2 = (
    (u'Диваны', 'sofas'),
    (u'Столы', 'tables'),
    (u'Кресла', 'armchairs'),
    (u'Стулья', 'chairs'),
)

rotang_level3 = (
    (u'Мини', 'mini'),
    (u'Стандарт', 'standard'),
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

vases = (
    (u'Cтекло', 'glass'),
    (u'Плетеные', 'pletenie'),
)
