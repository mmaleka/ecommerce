from django.shortcuts import render
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.http import Http404
from django.contrib.auth.decorators import login_required

@login_required
def order_create(request):

    cart = Cart(request)
    orders = Order.objects.all()
    last_order = orders[0]
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            print("form.cleaned_data['shipping']: ", form.cleaned_data['shipping'])
            first_name = request.user.first_name
            last_name = request.user.last_name
            email = request.user.email


            # order = form.save(commit=False)

            address = form.cleaned_data['address']
            postal_code = form.cleaned_data['postal_code']
            city = form.cleaned_data['city']
            # total_price_with_shipping = form.cleaned_data['total_price_with_shipping']
            payment_method = form.cleaned_data['payment_method']

            if form.cleaned_data['shipping'] == 'FD':
                total_price_with_shipping = float(cart.get_total_price_discountTOTAL())
            elif form.cleaned_data['shipping'] == 'PL':
                total_price_with_shipping = float(cart.get_total_price_discountTOTAL() + float(40))

            order = form.save(commit=False)

            order.first_name = first_name
            order.last_name = last_name
            order.email = email
            # order = form.save(commit=False)
            order.address = address
            order.postal_code = postal_code
            order.city = city
            order.total_price = total_price_with_shipping
            order.payment_method = payment_method

            order = form.save()
            # data = cleaned_data
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
        # else:
        #     raise Http404
        return render(request, 'orders/order/payment.html', {'order': order})

    else:
        form = OrderCreateForm()

    context = {
    'last_order': last_order,
    'form': form,
    'orders': orders
    }
    return render(request, 'orders/order/create.html', context)
