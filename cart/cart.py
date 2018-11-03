from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        total = sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
        return total

    def get_total_price_discountTOTAL(self):
        total = sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
        print("total: ", total)
        if total > 400:
            discount = float(total) * 0.1
            total_with_discount = float(total) * 0.9
            total = float("{0:.2f}".format(total_with_discount))
        else:
            total = sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
        return total

    def get_total_price_discountAMOUNT(self):
        total = sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
        if total > 400:
            discount = float(total) * 0.1
            discount = float("{0:.2f}".format(discount))
        else:
            discount = 0.0
            discount = float("{0:.2f}".format(discount))
        return discount

    def get_total_price_with_shipping(self):
        total = sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
        print("total: ", total)
        if total > 400:
            discount = float(total) * 0.1
            total_with_discount = float(total) * 0.9
            total = float("{0:.2f}".format(total_with_discount))
        else:
            total = sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
        return total + 40

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
