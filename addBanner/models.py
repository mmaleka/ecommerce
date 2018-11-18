from django.db import models
from django.urls import reverse
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from shop.models import Product
import sys

class AddBanner(models.Model):
    name = models.CharField(max_length=150, db_index=True)

    product = models.OneToOneField(Product, on_delete=models.CASCADE, default=13)

    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='addBanner/%Y/%m/%d', blank=True)

    add_is_active = models.BooleanField(default=True)

    description1 = models.TextField(blank=True, null=True)
    description2 = models.TextField(blank=True, null=True)
    description3 = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'addbanner'
        verbose_name_plural = 'addbanners'

    def save(self):
        #Opening the uploaded image
        im = Image.open(self.image)
        output = BytesIO()
        #Resize/modify the image
        im = im.resize( (800,400) )
        #after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)
        #change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
        super(AddBanner,self).save()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('addBanner:AddBanner_detail', args=[self.id, self.slug])



class AddBannerImage(models.Model):
    name = models.ForeignKey(AddBanner, on_delete=models.CASCADE, related_name='images')
    imageMore = models.ImageField(upload_to='addBanner/%Y/%m/%d', blank=True)

    def save(self):
        #Opening the uploaded image
        im = Image.open(self.imageMore)
        output = BytesIO()
        #Resize/modify the image
        im = im.resize( (500,500) )
        #after modifications, save it to the output
        im.save(output, format='JPEG', quality=100)
        output.seek(0)
        #change the imagefield value to be the newley modifed image value
        self.imageMore = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.imageMore.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
        super(AddBannerImage,self).save()







        #
