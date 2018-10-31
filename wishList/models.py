from django.db import models
from django.conf import settings
from shop.models import Product
from shop.models import ProductImage

# Create your models here.

User = settings.AUTH_USER_MODEL

class WishListManager(models.Manager):
    def new_or_get(self, request):
        wishList_id = request.session.get("wishList_id", None)
        qs = self.get_queryset().filter(id=wishList_id)
        if qs.count() == 1:
            new_obj = False
            wishList_obj = qs.first()
            if request.user.is_authenticated and wishList_obj.user is None:
                wishList_obj.user = request.user
                wishList_obj.save()
        else:
            new_obj = True
            wishList_obj = WishList.objects.new(user=request.user)
            request.session['wishList_id'] = wishList_obj.id

        return wishList_obj, new_obj

    def new(self, user=None):
        print(user)
        user_obj = None
        if user is not None:
            print(user.is_authenticated)
            if user.is_authenticated: #request.user.is_authenticated1
                user_obj = user
        return self.model.objects.create(user=user_obj)

class WishList(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(default=0.00, decimal_places=2, max_digits=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


    objects = WishListManager()

    def __str__(self):
        return str(self.id)
