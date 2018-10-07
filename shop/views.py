# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category, Product, ProductImage
from addBanner.models import AddBanner
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    search_term = ''
    category = None
    categories = Category.objects.all()
    adds = AddBanner.objects.all()
    products = Product.objects.filter(available=True)
    productsImage = ProductImage.objects.all()
    if 'search' in request.GET:
        search_term = request.GET['search']
        products = products.filter(name__icontains=search_term)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)



    # paginator = Paginator(queryset_list, 10)  # Show 10 contacts per page
    page = request.GET.get('page')

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
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'productsImages': productsImage,
    }
    return render(request, 'shop/product/product_list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    productsImage = ProductImage.objects.all()
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
        'productsImages': productsImage
    }
    return render(request, 'shop/product/detail.html', context)
