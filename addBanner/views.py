# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from .models import AddBanner, AddBannerImage
from shop.models import Product
import re
from ipware import get_client_ip
import json
from urllib.request import urlopen

#
# def AddBanner_list(request, category_slug=None):
#     # adds = AddBanner.objects.all()
#     adds = get_object_or_404(AddBanner, id=id, slug=slug, available=True)
#     addsImages = AddBannerImage.objects.all()
#
#
#     context = {
#         'adds': adds,
#         'addsImage': addsImage,
#     }
#
#     return render(request, 'addBanner/addDetail.html', context)


def AddBanner_detail(request, id, slug):

    add = get_object_or_404(AddBanner, id=id, slug=slug)
    addsImages = AddBannerImage.objects.filter(name=add.id)

    print("Product.id: ", add.product.id)
    product = get_object_or_404(Product, id=add.product.id)
    print("product: ", product.get_absolute_url)


    context = {
        'add': add,
        'addsImages': addsImages,
        'product': product,
    }

    return render(request, 'addBanner/addDetail.html', context)
