from django.shortcuts import render
from django.http import JsonResponse
from cart.cart import Cart
from payment.forms import ShippingForm
from payment.models import ShippingAddress
from store.forms import UserInfoForm
from store.models import Profile


# Create your views here.

def payment_success(request):

    return render(request, 'payment/payment_success.html')

def checkout(request):
    cart = Cart(request)
    products = cart.get_prods()
    quantities = cart.get_quants()
    total = cart.cart_total()

    if request.user.is_authenticated:
        # Current user
        current_user = Profile.objects.get(user__id=request.user.id)
        # Current user shipping info
        try:
            # Current user shipping info
            shipping_user = ShippingAddress.objects.get(user__id=request.user.id)

        except ShippingAddress.DoesNotExist:
            # If no shipping address exists, create a new one
            shipping_user = ShippingAddress(user=request.user)
            shipping_user.save()

        # main user form
        form = UserInfoForm(request.POST or None, instance=current_user)

        # user shipping form
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
    context = {
        "products": products,
        "quantities": quantities,
        "total": total,
        'shipping_form': shipping_form,
    }
    return render(request, 'payment/checkout.html',context)