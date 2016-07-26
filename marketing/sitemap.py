from catalog.models import Product
from django.contrib.flatpages.models import FlatPage
from django.contrib.sitemaps import Sitemap


class ProductSitemap(Sitemap):
    def items(self):
        return Product.active.all()


# class CategorySitemap(Sitemap):
#     def items(self):
#         return Category.active.all()


class FlatPageSitemap(Sitemap):
    def items(self):
        return FlatPage.objects.all()


SITEMAPS = {'products': ProductSitemap, 'flatpages': FlatPageSitemap}
