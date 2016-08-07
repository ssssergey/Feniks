# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
import search
from Feniks import settings
from django.contrib.auth.decorators import login_required
from forms import ProductReviewForm
from catalog.models import Product
from django.template.loader import render_to_string
import json
from django.http import HttpResponse


def results(request, template_name="search/results.html"):
    # get current search phrase
    q = request.GET.get('q', '')
    # get current page number. Set to 1 is missing or invalid
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1
    # retrieve the matching products
    matching = search.products(q).get('products')
    # generate the pagintor object
    paginator = Paginator(matching, settings.PRODUCTS_PER_PAGE)
    try:
        results = paginator.page(page).object_list
    except (InvalidPage, EmptyPage):
        results = paginator.page(1).object_list
    # store the search
    search.store(request, q)
    # the usual
    page_title = u'Результат поиска для: ' + q
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


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
