from django.conf import settings
from django.db import models
from shop.models import Product

# Create your models here.
class ViewsCount(models.Model):
    user = models.CharField(max_length=150, db_index=True)
    ip_address = models.CharField(max_length=220, blank=True, null=True)
    address = models.CharField(max_length=220, blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # product = models.OneToOneField(Product, on_delete=models.CASCADE)
    product = models.CharField(max_length=150, db_index=True)
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return "{}-{}".format(self.product, self.views_count)

    class Meta:
        ordering = ['-time_stamp']


# Create your models here.
class PostViewsCount(models.Model):
    user = models.CharField(max_length=150, db_index=True)
    ip_address = models.CharField(max_length=220, blank=True, null=True)
    address = models.CharField(max_length=220, blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # product = models.OneToOneField(Product, on_delete=models.CASCADE)
    post = models.CharField(max_length=150, db_index=True)
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return "{}-{}".format(self.post, self.views_count)

    class Meta:
        ordering = ['-time_stamp']


class RegisterCount(models.Model):
    ip_address = models.CharField(max_length=220, blank=True, null=True)
    address = models.CharField(max_length=220, blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return "{}-{}".format(self.ip_address, self.views_count)

    class Meta:
        ordering = ['-time_stamp']

class CartItemsCount(models.Model):
    user = models.CharField(max_length=150, db_index=True)
    ip_address = models.CharField(max_length=220, blank=True, null=True)
    address = models.CharField(max_length=220, blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # product = models.OneToOneField(Product, on_delete=models.CASCADE)
    cartItems = models.CharField(max_length=150, db_index=True)
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return "{}-{}".format(self.user, self.views_count)

    class Meta:
        ordering = ['-time_stamp']
