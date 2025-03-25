from django.shortcuts import render
from cart.cart import Cart
from payment.forms import ShippingForm
from payment.models import ShippingAddress

# Create your views here.

def payment_success(request):

    return render(request, 'payment/payment_success.html')

def checkout(request):
    cart = Cart(request)
    products = cart.get_prods()
    quantities = cart.get_quants()
    total = cart.cart_total()

    if request.user.is_authenticated:
        try:
            shipping_user = ShippingAddress.objects.get(user__id=request.user.id)

        except ShippingAddress.DoesNotExist:
            # If no shipping address exists, create a new one
            shipping_user = ShippingAddress(user=request.user)
            shipping_user.save()

        # user shipping form
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
    context = {
        "products": products,
        "quantities": quantities,
        "total": total,
        'shipping_form': shipping_form,
    }
    return render(request, 'payment/checkout.html', context)