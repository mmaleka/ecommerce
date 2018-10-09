# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.db.models import Q
from .models import Category, Product, ProductImage
from addBanner.models import AddBanner
from cart.forms import CartAddProductForm
from analytics.models import ViewsCount
import re
import json
from urllib.request import urlopen


def product_list(request, category_slug=None):
    search_term = ''
    category = None
    categories = Category.objects.all()
    adds = AddBanner.objects.all()
    products_list = Product.objects.filter(available=True).order_by("-updated_at")
    productsImage = ProductImage.objects.all()

    paginator = Paginator(products_list, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    products = paginator.get_page(page)

    query = request.GET.get("search")
    if query:
        products = products.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query)
        ).distinct

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'productsImages': productsImage,
        'search_term': search_term,
        'adds': adds

    }
    return render(request, 'shop/product/list.html', context)


def product_list_by_category(request, category_slug=None):
    categories = Category.objects.all()
    productsImage = ProductImage.objects.all()
    products_list = Product.objects.filter(available=True).order_by("-updated_at")


    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products_list = Product.objects.filter(category=category)

        paginator = Paginator(products_list, 25) # Show 25 contacts per page

        page = request.GET.get('page')
        products = paginator.get_page(page)

    query = request.GET.get("search")
    if query:
        products = products.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query)
        ).distinct

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'productsImages': productsImage,
    }
    return render(request, 'shop/product/product_list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    # Get user ip adress:
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)

    IP=data['ip']
    org=data['org']
    city = data['city']
    country=data['country']
    region=data['region']

    address = str(str(city)+'-'+str(country)+'-'+str(region))

    view, created = ViewsCount.objects.get_or_create(
        user = str(request.user),
        product = str(product),
        ip_address = str(IP),
        address = address
    )
    if view:
        view.views_count += 1
        view.save()



    productsImage = ProductImage.objects.all()
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
        'productsImages': productsImage
    }
    return render(request, 'shop/product/detail.html', context)
