# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.db.models import Q
from .models import Category, Product, ProductImage
from addBanner.models import AddBanner
from cart.forms import CartAddProductForm
from wishList.models import WishList
from analytics.models import ViewsCount
from comments.models import Comment
from comments.forms import CommentForm
import re
from ipware import get_client_ip
import json
from urllib.request import urlopen
import random


def get_ip(request):
    try:
        client_ip, is_routable = get_client_ip(request)
        if client_ip is None:
            ip = request.META.get("REMOTE_ADDR")
        else:
            if is_routable:
                ip = ip
            else:
                ip = ip
    except Exception as e:
        ip = ""

    return ip


def product_list(request, category_slug=None):
    search_term = ''
    category = None
    categories = Category.objects.all()
    adds = AddBanner.objects.all()
    products_list = Product.objects.filter(available=True).order_by("-updated_at")
    productsImage = ProductImage.objects.all()

    print(product_list)

    query = request.GET.get("search")
    if query:
        products_list = products_list.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query)
        ).distinct()


    paginator = Paginator(products_list, 10)  # Show 10 contacts per page
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)


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
        products_list = Product.objects.filter(category=category).order_by("-updated_at")

        query = request.GET.get("search")
        if query:
            products_list = products_list.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
            ).distinct()

        paginator = Paginator(products_list, 25) # Show 25 contacts per page

        page = request.GET.get('page')
        products = paginator.get_page(page)



    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'productsImages': productsImage,
    }
    return render(request, 'shop/product/product_list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    wishList_obj, new_obj = WishList.objects.new_or_get(request)
    wishList_obj_all = wishList_obj.products.all()
    print("wishList_obj_all: ", wishList_obj_all)


    ip_adress = get_ip(request)
    try:
        IP=ip_adress['ip']
        org=ip_adress['org']
        city = ip_adress['city']
        country=ip_adress['country']
        region=ip_adress['region']
    except Exception as e:
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

    initial_data = {
        "content_type": product.get_content_type,
        "object_id": product.id,
    }


    form = CommentForm(request.POST or None, request.FILES or None, initial=initial_data)
    if form.is_valid() and request.user.is_authenticated:
        c_type = form.cleaned_data.get("content_type")
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get("object_id")
        content_data = form.cleaned_data.get("content")
        model_pic = form.cleaned_data.get("image")
        new_comment, created = Comment.objects.get_or_create(
            user = request.user,
            content_type=content_type,
            object_id = obj_id,
            content=content_data,
            image=model_pic,
        )

        if created:
            print("yeah")


    content_type = ContentType.objects.get_for_model(Product)
    obj_id = product.id
    comments_list = Comment.objects.filter_by_product(product).order_by("-timestamp")

    paginator = Paginator(comments_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    comments = paginator.get_page(page)

    products_list = Product.objects.filter(available=True).order_by("-updated_at")
    # productsImage = ProductImage.objects.all()
    products_list_random = random.sample(list(products_list), min(len(products_list), 5))

    productsImage = ProductImage.objects.all()
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
        'productsImages': productsImage,
        'comments': comments,
        'comment_form': form,
        'wishList': wishList_obj_all,
        'products_list_random': products_list_random,
    }
    return render(request, 'shop/product/detail.html', context)
