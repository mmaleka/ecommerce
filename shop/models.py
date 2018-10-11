from django.db import models
from django.urls import reverse
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.contenttypes.models import ContentType
import sys



class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slogan = models.CharField(max_length=150, default='Hot items, Affordable prices')
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    warranty = models.CharField(max_length=100, default='Limited (12 months)')

    # shipping_Choices = (
    # ('FD', 'Free delivery available in South Africa only'),
    # ('PR', 'Payment received'),
    # ('PO', 'Processing order'),
    # ('ID', 'Items dispatched'),
    # ('IR', 'Items received'),
    # )
    #
    # shipping = models.CharField(max_length=2, choices=shipping_Choices, default='Free delivery available in South Africa only')
    shipping = models.TextField(default='Free delivery available in South Africa only')
    barcode = models.CharField(max_length=100, default='No barcode yet')

    productUrl = models.CharField(max_length=220, default="https://www.aliexpress.com/")

    # image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    @property
    def get_content_type(self):
        product = self
        content_type=ContentType.objects.get_for_model(product.__class__)
        return content_type

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    def save(self):
        #Opening the uploaded image
        im = Image.open(self.image)
        output = BytesIO()
        #Resize/modify the image
        im = im.resize( (500,500) )
        #after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)
        #change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
        super(ProductImage,self).save()
