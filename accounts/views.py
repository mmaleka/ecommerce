from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .forms import UserLoginForm, UserRegisterForm
# from posts.models import Post
from orders.models import Order, OrderItem
# from accounts.forms import RegistrationForm
from shop.models import Product, ProductImage
from analytics.models import RegisterCount
import re
import json
from urllib.request import urlopen
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.




def login_view(request):
    print(request.user.is_authenticated)
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    print("request.user.is_authenticated1", request.user.is_authenticated)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        print("request.user.is_authenticated2", request.user.is_authenticated)
        # Redirect here
        if next:
            return redirect(next)
        return redirect('shop:product_list')

    context = {
        "form": form,
        "title": "Login",
    }

    return render(request, 'accounts/form.html', context)


def register_view(request):
    form = UserRegisterForm(request.POST or None)

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

    view, created = RegisterCount.objects.get_or_create(
        ip_address = str(IP),
        address = address
    )
    if view:
        view.views_count += 1
        view.save()

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('shop:product_list')

    context = {
                'title': 'Sign Up',
                'form': form,
            }
    return render(request, "accounts/form.html", context)

# def register_view(request):
#     next = request.GET.get('next')
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             if next:
#                 return redirect(next)
#             return redirect('shop:product_list')
#     else:
#         form = RegistrationForm()
#         context = {
#             'title': 'Sign Up',
#             'form': form,
#         }
#         return render(request, "accounts/form.html", context)


def logout_view(request):
    logout(request)
    return redirect('shop:product_list')


@login_required
def profile_view(request):

    orders_list = Order.objects.filter(first_name=request.user.first_name)
    orderItems = OrderItem.objects.all()
    productImage = ProductImage.objects.all()
    product = Product.objects.all()

    paginator = Paginator(orders_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    orders = paginator.get_page(page)

    context = {
        'title': 'User Profile',
        'user': request.user,
        'orders': orders,
        'orderItems':orderItems,
        'productImages': productImage,
        'products': product,
    }

    return render(request, "accounts/profile.html", context)
