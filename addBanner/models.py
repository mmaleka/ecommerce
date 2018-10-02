from django.db import models
from django.urls import reverse


class AddBanner(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='addBanner/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'addbanner'
        verbose_name_plural = 'addbanners'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
