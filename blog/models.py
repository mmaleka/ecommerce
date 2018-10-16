from django.db import models
from django.urls import reverse
from django.conf import settings
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.contenttypes.models import ContentType
import sys
from tinymce import HTMLField



class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post:post_list_by_category', args=[self.slug])


class Post(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    # description = models.TextField(blank=True)
    # description = HTMLField()
    description = models.TextField(max_length=250,null=True)
    content = HTMLField('Content', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    draft = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog/%Y/%m/%d', blank=True, null=True)

    class Meta:
        ordering = ('title', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id, self.slug])

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
        super(Post,self).save()

    @property
    def get_content_type(self):
        post = self
        content_type=ContentType.objects.get_for_model(post.__class__)
        return content_type
