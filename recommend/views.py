# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from shop.models import Product, ProductImage
from analytics.models import ViewsCount
import re
from ipware import get_client_ip
import json
from urllib.request import urlopen


def recommended_product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).order_by("-updated_at")
    productsImage = ProductImage.objects.all()

    print(products)

    context = {
        'products': products,
        'productsImages': productsImage,
    }

    return render(request, 'recommend/recommended/recommended.html', context)
