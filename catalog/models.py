# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, AbstractUser

from django.db import models
from django_thumbs.db.models import ImageWithThumbsField
from django.utils import timezone

from Feniks import settings
from django.utils.text import slugify
from unidecode import unidecode
from django.db.models import Q


class ActiveCategoryManager(models.Manager):
    def get_query_set(self):
        return super(ActiveCategoryManager, self).get_query_set().filter(is_active=True)


class FeaturedProductManager(models.Manager):
    def all(self):
        return super(FeaturedProductManager, self).all().filter(is_active=True).filter(is_featured=True)


class ActiveProductManager(models.Manager):
    def get_query_set(self):
        return super(ActiveProductManager, self).get_query_set().filter(is_active=True)


class Material(models.Model):
    name = models.CharField(u'Название', max_length=100, blank=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = u'Материал'
        verbose_name_plural = u'Материалы'

    def __unicode__(self):
        return self.name


def image_upload_to(instance, filename):
    title = instance.name
    title_slug = slugify(unidecode(title))
    filename_list = filename.split(".")
    filename_slug = slugify(unidecode(filename_list[0]))
    new_filename = "%s.%s" % (title_slug + '-' + filename_slug, filename_list[1])
    return "images/products/%s" % (new_filename)


def image_architecture_upload_to(instance, filename):
    title = instance.name
    title_slug = slugify(unidecode(title))
    filename_list = filename.split(".")
    filename_slug = slugify(unidecode(filename_list[0]))
    new_filename = "%s.%s" % (title_slug + '-' + filename_slug, filename_list[1])
    return "images/architecture/%s" % (new_filename)


class Architecture(models.Model):
    name = models.CharField(u'Название', max_length=100, blank=True, unique=True)
    description = models.TextField(u'Описание', blank=True, null=True)
    image = models.ImageField(verbose_name=u'Анимация', upload_to=image_architecture_upload_to, blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = u'Конструкция'
        verbose_name_plural = u'Конструкция'

    def __unicode__(self):
        return self.name


class Product(models.Model):
    sku = models.CharField(u'Код', max_length=50, blank=True, null=True)
    MODULE_KOMPLEKT = (
        (u'Комплект', u'Комплект'), (u'Модуль', u'Модуль'), (u'Интерьер', u'Интерьер'), (u'Камин', u'Камин'),
        (u'Сопутствующие товары', u'Сопутствующие товары'),
    )
    module_komplekt = models.CharField(u'Общие категории', max_length=100, blank=True, choices=MODULE_KOMPLEKT)

    KOMPLEKT_MEBEL = (
        (u'Корпусная мебель', u'Корпусная мебель'), (u'Мягкая мебель', u'Мягкая мебель'),
        (u'Кухонный уголок', u'Кухонный уголок'), (u'Обеденная группа', u'Обеденная группа'),
        (u'Каминный комплект', u'Каминный комплект'),
    )
    komplekt_mebel = models.CharField(u'Тип мебели', max_length=100, blank=True, choices=KOMPLEKT_MEBEL)

    ROOM = (
        (u'Кухня', u'Кухня'), (u'Гостиная(горки, стенки)', u'Гостиная(горки, стенки)'), (u'Прихожие', u'Прихожие'),
        (u'Детские', u'Детские'), (u'Спальня', u'Спальня'), (u'Другое', u'Другое'),
    )
    room = models.CharField(u'Комната', max_length=100, blank=True, choices=ROOM)

    MODULE_MEBEL = (
        (u'Шкаф', u'Шкаф'), (u'Кровать', u'Кровать'), (u'Диван', u'Диван'), (u'Кресло', u'Кресло'), (u'Стул', u'Стул'),
        (u'Стол', u'Стол'), (u'ТВ-тумба', u'ТВ-тумба'), (u'Библиотека', u'Библиотека'), (u'Перегородка', u'Перегородка'),
        (u'Ресепшн', u'Ресепшн'), (u'Кухонный уголок', u'Кухонный уголок'), (u'Стойка', u'Стойка'),
        (u'Прилавок', u'Прилавок'), (u'Антресоль', u'Антресоль'), (u'Тумба', u'Тумба'), (u'Полка', u'Полка'),
    )
    module_mebel = models.CharField(u'Тип модуля мебели', max_length=100, blank=True, choices=MODULE_MEBEL)

    MODULE_OTHER = (
        (u'Камин-портал', u'Камин-портал'), (u'Камин-электрокамин', u'Камин-электрокамин'), (u'Камин-печь', u'Камин-печь'),
        (u'Камин-3D-камин', u'Камин-3D-камин'),
        (u'Камин-аксессуар', u'Камин-аксессуар'), (u'Матрас', u'Матрас'), (u'Качели', u'Качели'),
        (u'Раскладушка', u'Раскладушка'), (u'Шезлонг', u'Шезлонг'), (u'Цветы', u'Цветы'), (u'Статуэтка', u'Статуэтка'),
        (u'Картина', u'Картина'), (u'Ваза', u'Ваза'), (u'Корзина', u'Корзина'), (u'Сундук', u'Сундук'),
        (u'Электротовар', u'Электротовар'), (u'Смеситель', u'Смеситель'), (u'Плита', u'Плита'),
        (u'Холодильник', u'Холодильник'), (u'Мойка', u'Мойка'), (u'Фартук', u'Фартук'), (u'Разное', u'Разное'),
    )
    module_other = models.CharField(u'Другой тип модуля', max_length=100, blank=True, choices=MODULE_OTHER)

    DOORS = ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6),)
    doors = models.IntegerField(u'Количество дверей (шкаф)', blank=True, choices=DOORS, null=True)

    LENGTH_BED = ((0, 0), (80, 80), (90, 90), (120, 120), (140, 140), (160, 160), (180, 180),)
    length = models.IntegerField(u'Ширина кровати', blank=True, choices=LENGTH_BED, null=True)

    SOFT_KOMPLEKT = ((u'Диван + 2 кресла-кровати', u'Диван + 2 кресла-кровати'),
                     (u'Диван + 2 кресла + кресло-кровать', u'Диван + 2 кресла + кресло-кровать'),
                     (u'Диван-кровать + 2 кресла-кровати', u'Диван-кровать + 2 кресла-кровати'),
                     (u'Диван + 2 кресла глухих', u'Диван + 2 кресла глухих'),
                     (u'Диван + 2 кресла с ящиками', u'Диван + 2 кресла с ящиками'),
                     (u'Угловой диван + 1 кресло с ящиками', u'Угловой диван + 1 кресло с ящиками'),
                     (u'Глухой диван + 2 глухих кресла', u'Глухой диван + 2 глухих кресла'),
                     (u'Угловой диван + глухое кресло', u'Угловой диван + глухое кресло'),
                     (u'Угловой диван + кресло-кровать', u'Угловой диван + кресло-кровать'),
                     )
    soft_komplekt = models.CharField(u'Комплект мягкой мебели', max_length=100, blank=True, choices=SOFT_KOMPLEKT)

    # ARCHITECTURE_TYPE = (
    #     (u'Выкатные', u'Выкатные'), (u'Раскладные', u'Раскладные'), (u'Классические', u'Классические'),
    #     (u'Евро', u'Евро'), (u'Металлокаркас', u'Металлокаркас'), (u'Мини', u'Мини'),
    #     (u'Евро-книжка', u'Евро-книжка'), (u'Книжка', u'Книжка'), (u'Стандарт', u'Стандарт'), (u'Шкаф-купе', u'Шкаф-купе'),
    #     (u'Кресла-кровати', u'Кресла-кровати'), (u'Кресла-качалки', u'Кресла-качалки'), (u'Банкетки', u'Банкетки'),
    #     (u'Офисные', u'Офисные'), (u'Двухъярусная кровать', u'Двухъярусная кровать'), (u'Пружинные', u'Пружинные'),
    #     (u'Ортопедические', u'Ортопедические'), (u'Анатомические', u'Анатомические'), (u'Беспружинные', u'Беспружинные'),
    #     (u'Комплектующие', u'Комплектующие'), (u'Независимые пружины', u'Независимые пружины'),
    # )
    # architecture_type = models.CharField(u'Конструкция', max_length=100, blank=True, choices=ARCHITECTURE_TYPE)
    architecture_type = models.ManyToManyField(Architecture, verbose_name=u'Конструкция', blank=True)

    ARMCHAIRE_ROLE = (
        (u'Для руководителя', u'Для руководителя'), (u'Для персонала', u'Для персонала'),
        (u'Для менеджеров', u'Для менеджеров'),
    )
    armchaire_role = models.CharField(u'Тип офисного кресла', max_length=100, blank=True, choices=ARMCHAIRE_ROLE)

    STYLE = (
        (u'Офисные', u'Офисные'), (u'Садовые', u'Садовые'), (u'Для баров и ресторанов', u'Для баров и ресторанов'),
        (u'Банкетка', u'Банкетка'), (u'Для кинотеатров', u'Для кинотеатров'), (u'Для посетителей', u'Для посетителей'),
        (u'Под старину', u'Под старину'), (u'Гостиничные номера', u'Гостиничные номера'), (u'Обеденные', u'Обеденные'),
        (u'Компьютерные', u'Компьютерные'), (u'Журнальные', u'Журнальные'), (u'Туалетные', u'Туалетные'),
        (u'Письменные', u'Письменные')
    )
    style = models.CharField(u'Стиль', max_length=100, blank=True, choices=STYLE)

    MATERIAL = ((u'Деревянные', u'Деревянные'), (u'Металлокаркас', u'Металлокаркас'), (u'Пластиковые', u'Пластиковые'),
                (u'ЛДСП', u'ЛДСП'), (u'Стеклянные', u'Стеклянные'), (u'Натуральный мрамор', u'Натуральный мрамор'),
                (u'Полимерный камень', u'Полимерный камень'), (u'МДФ', u'МДФ'), (u'Плетеные', u'Плетеные'),
                (u'Ротанг', u'Ротанг'),
                (u'Ротанг искусственный', u'Ротанг искусственный'), (u'Ротанг натуральный', u'Ротанг натуральный'))
    # material = models.CharField(u'Материал', max_length=100, blank=True, choices=MATERIAL)
    material = models.ManyToManyField(Material, verbose_name=u'Материал', blank=True)

    SHAPE = ((u'Круглые', u'Круглые'), (u'Овальные', u'Овальные'), (u'Прямоугольные', u'Прямоугольные'),
             (u'Квадратные', u'Квадратные'), (u'Угловые', u'Угловые'), (u'Прямые', u'Прямые'), (u'П-образные', u'П-образные'),)
    shape = models.CharField(u'Форма', max_length=100, blank=True, choices=SHAPE)

    BRAND = (
        ('Castle', 'Castle'), ('Stone', 'Stone'), ('Classic', 'Classic'), ('New Look', 'New Look'), ('Mini', 'Mini'),
        ('Marble', 'Marble'))
    brand = models.CharField(u'Брэнд', max_length=100, blank=True, choices=BRAND)

    OCHAG = ((u'Широкий очаг', u'Широкий очаг'), (u'Стандартный очаг', u'Стандартный очаг'),
             (u'Навесной очаг', u'Навесной очаг'),)
    ochag = models.CharField(u'Очаг каминов', max_length=100, blank=True, choices=OCHAG)
    peace_of = models.ManyToManyField('self', verbose_name=u'Относится к комплекту',
                                      # limit_choices_to={'module_komplekt': u'Комплект'},
                                      unique=False, null=True, blank=True)

    name = models.CharField(u'Название товара', max_length=255)
    slug = models.SlugField(max_length=255, unique=True,
                            help_text='Unique value for product page URL, created from name.')
    image = ImageWithThumbsField(verbose_name=u'Фото_1', upload_to=image_upload_to, blank=True,
                                 sizes=((300, 200), (400, 200), (180, 200), (180, 150)))
    image2 = ImageWithThumbsField(verbose_name=u'Фото_2', upload_to=image_upload_to, blank=True,
                                  sizes=((300, 200), (400, 200), (180, 200), (180, 150)))
    image3 = ImageWithThumbsField(verbose_name=u'Фото_3', upload_to=image_upload_to, blank=True,
                                  sizes=((300, 200), (400, 200), (180, 200), (180, 150)))
    image4 = ImageWithThumbsField(verbose_name=u'Фото_4', upload_to=image_upload_to, blank=True,
                                  sizes=((300, 200), (400, 200), (180, 200), (180, 150)))
    image5 = ImageWithThumbsField(verbose_name=u'Фото_5', upload_to=image_upload_to, blank=True,
                                  sizes=((300, 200), (400, 200), (180, 200), (180, 150)))
    country = models.CharField(u'Страна-производитель', max_length=50, blank=True)
    price = models.IntegerField(u'Цена', null=True)
    price_bulk1 = models.IntegerField(u'Оптовая цена 1', blank=True, null=True)
    # price_bulk2 = models.IntegerField(u'Оптовая цена 2', blank=True, null=True)
    # price_bulk3 = models.IntegerField(u'Оптовая цена 3', blank=True, null=True)
    # categories = models.ManyToManyField(Category, verbose_name=u'Категории')
    # quantity = models.IntegerField(u'Количество', default=1)
    description = models.TextField(u'Описание', blank=True)
    garantee = models.IntegerField(u'Гарантийный срок', blank=True, default=12)
    on_order = models.BooleanField(u'Под заказ', default=False)
    is_bestseller = models.BooleanField(u'Хит продаж', default=False)
    is_featured = models.BooleanField(u'Выгодно', default=False)

    created_at = models.DateTimeField(u'Создан', auto_now_add=True)
    updated_at = models.DateTimeField(u'Изменен', auto_now=True)
    meta_keywords = models.CharField(u'Мета ключевые слова', max_length=255,
                                     help_text=u'Разделенные запятой слова для SEO, не более пяти.', blank=True)
    meta_description = models.TextField(u'Мета описание', help_text=u'Для описательного мета-тэга', blank=True)
    is_active = models.BooleanField(u'Активно', default=True)
    objects = models.Manager()
    active = ActiveProductManager()
    featured = FeaturedProductManager()

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']
        verbose_name = u'Товар'
        verbose_name_plural = u'Товары'

    def __unicode__(self):
        return u'Товар: {}'.format(self.name)

    def get_absolute_url(self):
        return reverse('catalog_product', args=(self.slug,))

    def new(self):
        delta = timezone.now() - self.created_at
        if delta.days < 10:
            return True
        else:
            return False

    def admin_image(self):
        if self.image:
            return u'<img src="%s" width="100"/>' % self.image.url_180x200
        else:
            return u'(Нет)'

    admin_image.allow_tags = True

    def get_related_modules(self):
        modules = Product.active.filter(peace_of=self)
        return modules

        # def get_parent_komplekt(self):
        #     komplekt = self.peace_of
        #     return komplekt
