from django.db import models
from shop.models import Product, ProductImage


class Order(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    payment_Choices = (
    ('EP', 'EFT Payment'),
    ('DP', 'Payment on delivery'),
    )
    payment_method = models.CharField(max_length=2, choices=payment_Choices, default='Pay on delivery')
    paid = models.BooleanField(default=False)
    status_Choices = (
    ('PP', 'Processing payment'),
    ('PR', 'Payment received'),
    ('PO', 'Processing order'),
    ('ID', 'Items dispatched'),
    ('IR', 'Items received'),
    )
    status = models.CharField(max_length=2, choices=status_Choices, default='Processing payment')

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    productImage = models.ForeignKey(ProductImage, related_name='order_items_images',
    on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
