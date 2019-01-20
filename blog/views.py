# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.db.models import Q
from .models import Category, Post
from analytics.models import PostViewsCount
from comments.models import Comment
from comments.forms import CommentForm
from recommend.views import recommended_product_list
from shop.models import Category, Product, ProductImage
from shop.views import get_ip
import re
import json
from urllib.request import urlopen
import random



def post_list(request, category_slug=None):
    search_term = ''
    category = None
    categories = Category.objects.all()
    post_list = Post.objects.filter(draft=False).order_by("-updated_at")

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = Post.objects.filter(category=category).order_by("-updated_at")

    query = request.GET.get("search")
    if query:
        post_list = post_list.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query) |
        Q(content__icontains=query)
        ).distinct()

        # print("post_list2: ", post_list)

    paginator = Paginator(post_list, 10) # Show 10 contacts per page

    page = request.GET.get('page')
    posts = paginator.get_page(page)

    # print(posts)
    context = {
        'category': category,
        'categories': categories,
        'posts': posts,
        'search_term': search_term,

    }
    return render(request, 'posts/post_list.html', context)

def post_detail(request, id, slug):
    # print("ip_address: ", request.META.get("REMOTE_ADDR"))
    # print("ip_address x_forwared_for: ", request.META.get("HTTP_X_FORWARED_FOR"))

    post_list = Post.objects.filter(draft=False).order_by("-updated_at")
    post = get_object_or_404(Post, id=id, slug=slug)

    products_list = Product.objects.filter(available=True).order_by("-updated_at")
    productsImage = ProductImage.objects.all()
    products_list_random = random.sample(list(products_list), min(len(products_list), 4))


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
    # print("address: ", address)

    view, created = PostViewsCount.objects.get_or_create(
        user = str(request.user),
        post = str(post),
        ip_address = str(IP),
        address = address
    )
    if view:
        view.views_count += 1
        view.save()

    initial_data = {
        "content_type": post.get_content_type,
        "object_id": post.id,
    }

    print("initial_data: ", initial_data)


    form = CommentForm(request.POST or None, request.FILES or None, initial=initial_data)
    if form.is_valid() and request.user.is_authenticated:
        c_type = form.cleaned_data.get("content_type")
        print("c_type: ", c_type)
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


    content_type = ContentType.objects.get_for_model(Post)
    obj_id = post.id
    comments_list = Comment.objects.filter_by_product(post).order_by("-timestamp")

    paginator = Paginator(comments_list, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    comments = paginator.get_page(page)

    context = {
        'post_list': post_list,
        'post': post,
        'comments': comments,
        'comment_form': form,
        'products_list_random': products_list_random,
        'productsImages': productsImage,
    }
    return render(request, 'posts/post_detail.html', context)
