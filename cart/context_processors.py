from . cart import Cart
# crete context processor so our cart can work on all pages

def cart(request):
    # return default data from Cart
    return {'cart': Cart(request)}