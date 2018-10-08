from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product, ProductImage
from .cart import Cart
from .forms import CartAddProductForm
from analytics.models import CartItemsCount
import re
import json
from urllib.request import urlopen


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    cartItems = []
    cartProducts = []
    for item in cart:
        print(item)
        cartItems.append(item)
        for k, v in item.items():
            print(k, v)
    print(cartItems)

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

    view, created = CartItemsCount.objects.get_or_create(
        user = str(request.user),
        cartItems = str(cartItems),
        ip_address = str(IP),
        address = address
    )
    if view:
        view.views_count += 1
        view.save()

    productsImage = ProductImage.objects.all()
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    context = {
        'cart': cart,
        'productsImages': productsImage
    }
    return render(request, 'cart/detail.html', context)
