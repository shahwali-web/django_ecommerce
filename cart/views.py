from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse


# Create your views here.

def cart_summary(request):
    # get cart
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    context = {
        "cart_products": cart_products,
        "quantities": quantities,
    }
    return render(request, 'cart_summary.html', context)

def cart_add(request):
    # get the cart
    cart = Cart(request)
    #test for post
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        # save to session
        cart.add(product=product, quantity=product_qty)

        # Get cart Number value
        cart_quantity = cart.__len__()
        return JsonResponse({'qty': cart_quantity})


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)
        return JsonResponse({'qty':product_qty})
def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        cart.delete(product=product_id)
        return JsonResponse({'qty': product_id})

