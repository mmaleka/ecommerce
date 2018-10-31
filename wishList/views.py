from django.shortcuts import render, redirect
from .models import WishList
from shop.models import Product
from shop.models import ProductImage
# Create your views here.

def wishList_create(user=None):
    wishList_obj = WishList.objects.create(user=None)
    return wishList_obj


def wishList_detail(request):
    wishList_obj, new_obj = WishList.objects.new_or_get(request)
    products = wishList_obj.products.all()
    total = 0
    for x in products:
        total += x.price
    print(total)
    wishList_obj.total = total + 10
    wishList_obj.save()

    return render(request, "wishList.html", {})

def wishList_update(request):
    print("request.POST: ", request.POST)
    product_id = 14
    product_obj = Product.objects.get(id=product_id)
    wishList_obj, new_obj = WishList.objects.new_or_get(request)
    if product_obj in wishList_obj.products.all():
        wishList_obj.products.remove(product_obj)
    else:
        wishList_obj.products.add(product_obj)
    # wishList_obj.products.remove(obj)
    return redirect(product_obj.get_absolute_url())
    # return redirect('wishList:home')
