# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.db import models
from django_thumbs.db.models import ImageWithThumbsField


class ActiveCategoryManager(models.Manager):
    def get_query_set(self):
        return super(ActiveCategoryManager, self).get_query_set().filter(is_active=True)


class FeaturedProductManager(models.Manager):
    def all(self):
        return super(FeaturedProductManager, self).all().filter(is_active=True).filter(is_featured=True)


class ActiveProductManager(models.Manager):
    def get_query_set(self):
        return super(ActiveProductManager, self).get_query_set().filter(is_active=True)


class ActiveProductReviewManager(models.Manager):
    def all(self):
        return super(ActiveProductReviewManager, self).all().filter(is_approved=True)


# class Category(models.Model):
#     name = models.CharField(u'Название категории', max_length=50)
#     slug = models.SlugField(max_length=50, unique=True,
#                             help_text='Unique value for product page URL, created from name.')
#     is_active = models.BooleanField(u'Активна', default=True)
#     created_at = models.DateTimeField(u'Создана', auto_now_add=True)
#     updated_at = models.DateTimeField(u'Изменена', auto_now=True)
#     objects = models.Manager()
#     active = ActiveCategoryManager()
#
#     class Meta:
#         db_table = 'categories'
#         ordering = ['-created_at']
#         verbose_name = u'Категория'
#         verbose_name_plural = u'Категории'
#
#     def __unicode__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse('catalog_category', args=(self.slug,))


class Product(models.Model):
    # KORP_MEBEL = ((u'Кухни', u'Кухни'), (u'Горки, стенки, гостинные', u'Горки, стенки, гостинные'),
    #               (u'Спальни', u'Спальни'), (u'Прихожие', u'Прихожие'),
    #               (u'Детские', u'Детские'), (u'Другая мебель', u'Другая мебель'), (u'Шкафы', u'Шкафы'),
    #               (u'Кровати', u'Кровати'), (u'ТВ-тумбы', u'ТВ-тумбы'),
    #               )
    # korp_mebel = models.CharField(u'КОРПУСНАЯ МЕБЕЛЬ', max_length=100, blank=True, choices=KORP_MEBEL)
    # SOFT_MEBEL = ((u'Комплекты', u'Комплекты'), (u'Угловые', u'Угловые'),
    #               (u'Диваны', u'Диваны'), (u'Кресла', u'Кресла'), (u'Под заказ', u'Под заказ'),
    #               )
    # soft_mebel = models.CharField(u'МЯГКАЯ МЕБЕЛЬ', max_length=100, blank=True, choices=SOFT_MEBEL)
    #
    # OFFICE_MEBEL = ((u'Диваны', u'Диваны'), (u'Столы', u'Столы'), (u'Шкафы', u'Шкафы'), (u'Библиотеки', u'Библиотеки'),
    #                 (u'Кресла', u'Кресла'), (u'Стулья', u'Стулья'), (u'Перегородки', u'Перегородки'),
    #                 )
    # office_mebel = models.CharField(u'Тип ОФИСНОЙ МЕБЕЛИ', max_length=100, blank=True, choices=OFFICE_MEBEL)
    # CAMINS = ((u'Каминные комплекты', u'Каминные комплекты'), (u'Серии', u'Серии'), (u'Порталы', u'Порталы'),
    #           (u'Электрокамины', u'Электрокамины'), (u'Печи', u'Печи'), (u'Аксессуары', u'Аксессуары'),
    #           )
    # camins = models.CharField(u'Тип КАМИНОВ', max_length=100, blank=True, choices=CAMINS)
    #
    # TABLES = ((u'Раскладные', u'Раскладные'), (u'Нераскладные', u'Нераскладные'),
    #           )
    # tables = models.CharField(u'Тип СТОЛОВ', max_length=100, blank=True, choices=TABLES)
    #
    # CHAIRS = ((u'Деревянные', u'Деревянные'), (u'Металлокаркас', u'Металлокаркас'), (u'Пластиковые', u'Пластиковые'),
    #           (u'Разные', u'Разные'), (u'Барные', u'Барные'), (u'Складные', u'Складные'),
    #           )
    # chairs = models.CharField(u'Тип СТУЛЬЕВ', max_length=100, blank=True, choices=CHAIRS)
    #
    # KITCHEN_CONNERS = ((u'Комплекты', u'Комплекты'), (u'Модульно', u'Модульно'),
    #                    (u'Кухонные + угловые диваны', u'Кухонные + угловые диваны'),
    #                    (u'Уголки от', u'Уголки от'),
    #                    )
    # kitchen_conners = models.CharField(u'Тип КУХОННЫХ УГОЛКОВ', max_length=100, blank=True, choices=KITCHEN_CONNERS)
    #
    # MATRAC = (
    #     (u'Пружинные', u'Пружинные'), (u'Ортопедические', u'Ортопедические'), (u'Анатомические', u'Анатомические'),
    # )
    # matrac = models.CharField(u'Тип МАТРАСОВ', max_length=100, blank=True, choices=MATRAC)
    # GARDEN_MEBEL = (
    #     (u'Ротанг', u'Ротанг'), (u'Качели', u'Качели'), (u'Раскладушки', u'Раскладушки'), (u'Кресла', u'Кресла'),
    #     (u'Шезлонги', u'Шезлонги'), (u'Другое', u'Другое'),
    # )
    # garden_mebel = models.CharField(u'Тип САДОВОЙ МЕБЕЛИ', max_length=100, blank=True, choices=GARDEN_MEBEL)
    # FOR_BARS = (
    #     (u'Столы', u'Столы'), (u'Стулья', u'Стулья'), (u'Диваны', u'Диваны'), (u'Под старину', u'Под старину'),
    #     (u'Стойки', u'Стойки'),
    # )
    # for_bars = models.CharField(u'Для баров и ресторанов', max_length=100, blank=True, choices=FOR_BARS)
    #
    # INTERIER = (
    #     (u'Цветы', u'Цветы'), (u'Статуэтки', u'Статуэтки'), (u'Картины', u'Картины'), (u'Вазы', u'Вазы'),
    #     (u'Корзины', u'Корзины'),
    # )
    # interier = models.CharField(u'Интерьер', max_length=100, blank=True, choices=INTERIER)
    #
    # SOPUT_TOVARI = (
    #     (u'Электротовары', u'Электротовары'), (u'Смесители', u'Смесители'), (u'Плиты', u'Плиты'),
    #     (u'Холодильники', u'Холодильники'), (u'Мойки', u'Мойки'), (u'Фартуки', u'Фартуки'),
    # )
    # soput_tovari = models.CharField(u'Сопутствующие товары', max_length=100, blank=True, choices=SOPUT_TOVARI)



    MODULE_KOMPLEKT = (
        (u'Комплект', u'Комплект'), (u'Модуль', u'Модуль'), (u'Интерьер', u'Интерьер'),
    )
    module_komplekt = models.CharField(u'Модуль, комплект или интерьер', max_length=100, blank=True,
                                       choices=MODULE_KOMPLEKT)

    KOMPLEKT_MEBEL = (
        (u'Корпусная мебель', u'Корпусная мебель'), (u'Мягкая мебель', u'Мягкая мебель'),
    )
    komplekt_mebel = models.CharField(u'Тип комплекта', max_length=100, blank=True, choices=KOMPLEKT_MEBEL)

    ROOM = (
        (u'Кухня', u'Кухня'), (u'Гостиная(горки, стенки)', u'Гостиная(горки, стенки)'), (u'Прихожие', u'Прихожие'),
        (u'Детские', u'Детские'),
    )
    room = models.CharField(u'Комната', max_length=100, blank=True, choices=ROOM)

    MODULE_MEBEL = (
        (u'Шкаф', u'Шкаф'), (u'Кровать', u'Кровать'), (u'Диван', u'Диван'), (u'Кресло', u'Кресло'), (u'Стул', u'Стул'),
        (u'Стол', u'Стол'), (u'ТВ-тумба', u'ТВ-тумба'), (u'Библиотека', u'Библиотека'),
        (u'Перегородка', u'Перегородка'),
        (u'Ресепшн', u'Ресепшн'), (u'Кухонный уголок', u'Кухонный уголок'), (u'Стойка', u'Стойка'),
        (u'Прилавок', u'Прилавок'),
    )
    module_mebel = models.CharField(u'Тип модуля мебели', max_length=100, blank=True, choices=MODULE_MEBEL)

    MODULE_OTHER = (
        (u'Камин-портал', u'Камин-портал'), (u'Камин-электрокамин', u'Камин-электрокамин'),
        (u'Камин-печь', u'Камин-печь'),
        (u'Камин-аксессуар', u'Камин-аксессуар'), (u'Матрас', u'Матрас'), (u'Качели', u'Качели'),
        (u'Раскладушка', u'Раскладушка'), (u'Шезлонг', u'Шезлонг'), (u'Цветы', u'Цветы'), (u'Статуэтка', u'Статуэтка'),
        (u'Картина', u'Картина'), (u'Ваза', u'Ваза'), (u'Корзина', u'Корзина'), (u'Сундук', u'Сундук'),
        (u'Электротовар', u'Электротовар'), (u'Смеситель', u'Смеситель'), (u'Плита', u'Плита'),
        (u'Холодильник', u'Холодильник'),
        (u'Мойка', u'Мойка'), (u'Фартук', u'Фартук'), (u'Другое', u'Другое'),
    )
    module_other = models.CharField(u'Другой тип модуля', max_length=100, blank=True, choices=MODULE_OTHER)

    DOORS = ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6),)
    doors = models.IntegerField(u'Количество дверей (шкаф)', blank=True, choices=DOORS, default=0)

    LENGTH_BED = ((0, 0), (80, 80), (90, 90), (120, 120), (140, 140), (160, 160), (180, 180),)
    length = models.IntegerField(u'Длина кровати', blank=True, choices=LENGTH_BED, default=0)

    SOFT_KOMPLEKT = ((u'Диван + 2 кресла-кровати', u'Диван + 2 кресла-кровати'),
                     (u'Диван + 2 кресла + кресло-кровать', u'Диван + 2 кресла + кресло-кровать'),
                     (u'Диван-кровать + 2 кресла-кровати', u'Диван-кровать + 2 кресла-кровати'),
                     (u'Глухой диван + 2 глухих кресла', u'Глухой диван + 2 глухих кресла'),
                     (u'Угловой диван + глухое кресло', u'Угловой диван + глухое кресло'),
                     (u'Угловой диван + кресло-кровать', u'Угловой диван + кресло-кровать'),
                     )
    soft_komplekt = models.CharField(u'Комплект мягкой мебели', max_length=100, blank=True, choices=SOFT_KOMPLEKT)

    ARCHITECTURE_TYPE = (
        (u'Выкатные', u'Выкатные'), (u'Раскладные', u'Раскладные'), (u'Классические', u'Классические'),
        (u'Евро', u'Евро'),
        (u'Евро-книжка', u'Евро-книжка'), (u'Книжка', u'Книжка'), (u'Мини', u'Мини'), (u'Шкаф-купе', u'Шкаф-купе'),
        (u'Кресла-кровати', u'Кресла-кровати'), (u'Кресла-качалки', u'Кресла-качалки'), (u'Банкетки', u'Банкетки'),
        (u'Офисные', u'Офисные'), (u'Двухъярусная кровать', u'Двухъярусная кровать'), (u'Пружинные', u'Пружинные'),
        (u'Ортопедические', u'Ортопедические'), (u'Анатомические', u'Анатомические'),
    )
    architecture_type = models.CharField(u'Конструкция', max_length=100, blank=True, choices=ARCHITECTURE_TYPE)

    ARMCHAIRE_ROLE = (
        (u'Для руководителя', u'Для руководителя'), (u'Для персонала', u'Для персонала'),
        (u'Для менеджеров', u'Для менеджеров'),
    )
    armchaire_role = models.CharField(u'Тип кресла', max_length=100, blank=True, choices=ARMCHAIRE_ROLE)

    STYLE = (
        (u'Офисные', u'Офисные'), (u'Садовые', u'Садовые'), (u'Для баров и ресторанов', u'Для баров и ресторанов'),
        (u'Банкетка', u'Банкетка'), (u'Для кинотеатров', u'Для кинотеатров'), (u'Для посетителей', u'Для посетителей'),
        (u'Под старину', u'Под старину'),
    )
    style = models.CharField(u'Стиль', max_length=100, blank=True, choices=STYLE)

    MATERIAL = ((u'Деревянные', u'Деревянные'), (u'Металлокаркас', u'Металлокаркас'), (u'Пластиковые', u'Пластиковые'),
                (u'ЛДСП', u'ЛДСП'), (u'Стеклянные', u'Стеклянные'), (u'Натуральный мрамор', u'Натуральный мрамор'),
                (u'Полимерный камень', u'Полимерный камень'), (u'МДФ', u'МДФ'), (u'Плетеные', u'Плетеные'),
                (u'Ротанг искусственный', u'Ротанг искусственный'), (u'Ротанг натуральный', u'Ротанг натуральный'))
    materal = models.CharField(u'Материал', max_length=100, blank=True, choices=MATERIAL)

    SHAPE = ((u'Круглые', u'Круглые'), (u'Овальные', u'Овальные'), (u'Прямоугольные', u'Прямоугольные'),
             (u'Угловой', u'Угловой'), (u'Прямой', u'Прямой'),)
    shape = models.CharField(u'Форма', max_length=100, blank=True, choices=SHAPE)

    BRAND = (
        ('Castle', 'Castle'), ('Stone', 'Stone'), ('Classic', 'Classic'), ('New Look', 'New Look'), ('Mini', 'Mini'),
        ('Marble', 'Marble'))
    brand = models.CharField(u'Брэнд', max_length=100, blank=True, choices=BRAND)

    OCHAG = ((u'Широкий очаг', u'Широкий очаг'), (u'Стандартный очаг', u'Стандартный очаг'),
             (u'Навесной очаг', u'Навесной очаг'),)
    ochag = models.CharField(u'Очаг каминов', max_length=100, blank=True, choices=OCHAG)
    rotang = models.BooleanField(u'Ротанг', default=False)
    peace_of = models.ForeignKey('self', limit_choices_to={'module_komplekt': u'Комплект'}, unique=False, null=True,
                                 blank=True)

    name = models.CharField(u'Название товара', max_length=255)
    slug = models.SlugField(max_length=255, unique=True,
                            help_text='Unique value for product page URL, created from name.')
    image = ImageWithThumbsField(u'Большое фото', upload_to='images/products/main', blank=True,
                                 sizes=((125, 125), (200, 200)))
    country = models.CharField(u'Страна-производитель', max_length=50, blank=True)
    price = models.IntegerField(u'Цена', default=0)
    price_bulk1 = models.IntegerField(u'Оптовая цена 1', blank=True, default=0)
    price_bulk2 = models.IntegerField(u'Оптовая цена 2', blank=True, default=0)
    price_bulk3 = models.IntegerField(u'Оптовая цена 3', blank=True, default=0)
    # categories = models.ManyToManyField(Category, verbose_name=u'Категории')
    quantity = models.IntegerField(u'Количество', default=1)
    description = models.TextField(u'Описание', blank=True)
    garantee = models.IntegerField(u'Гарантийный срок', blank=True, default=12)
    on_order = models.BooleanField(u'Под заказ', default=False)
    is_active = models.BooleanField(u'В наличии', default=True)
    is_bestseller = models.BooleanField(u'Хит продаж', default=False)
    is_featured = models.BooleanField(u'Выгодно', default=False)

    created_at = models.DateTimeField(u'Создан', auto_now_add=True)
    updated_at = models.DateTimeField(u'Изменен', auto_now=True)
    meta_keywords = models.CharField(u'Мета ключевые слова', max_length=255,
                                     help_text=u'Разделенные запятой слова для SEO, не более пяти.', blank=True)
    meta_description = models.TextField(u'Мета описание', help_text=u'Для описательного мета-тэга', blank=True)
    objects = models.Manager()
    active = ActiveProductManager()
    featured = FeaturedProductManager()

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']
        verbose_name = u'Товар'
        verbose_name_plural = u'Товары'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog_product', args=(self.slug,))


class ProductReview(models.Model):
    RATINGS = ((5, 5), (4, 4), (3, 3), (2, 2), (1, 1),)
    product = models.ForeignKey(Product, verbose_name=u'Товар')
    user = models.ForeignKey(User, verbose_name=u'Пользователь')
    date = models.DateTimeField(u'Создан', auto_now_add=True)
    rating = models.PositiveSmallIntegerField(u'Рейтинг', default=5, choices=RATINGS)
    is_approved = models.BooleanField(u'Одобрен', default=True)
    content = models.TextField(u'Текст')
    objects = models.Manager()
    approved = ActiveProductReviewManager()

    class Meta:
        verbose_name = u'Отзыв'
        verbose_name_plural = u'Отзывы'