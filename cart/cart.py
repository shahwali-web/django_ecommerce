from store.models import Product, Profile


class Cart:
    def __init__(self, request):
        self.session = request.session
        self.request = request

        # get Current Session Key
        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # now Cart is available in every page
        self.cart = cart

    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)

        if product_id not in self.cart:
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        # deal login user session data
        if self.request.user.is_authenticated:
            # GET CURRENT USER PROFILE
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            session_cart_to_db = str(self.cart)
            single__to_double_quote = session_cart_to_db.replace("\'", "\"")
            current_user.update(logout_car=single__to_double_quote)

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

        # deal login user session data
        if self.request.user.is_authenticated:
            # GET CURRENT USER PROFILE
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            session_cart_to_db = str(self.cart)
            single__to_double_quote = session_cart_to_db.replace("\'", "\"")
            current_user.update(logout_car=single__to_double_quote)

    def __len__(self):
        return len(self.cart)

    def get_prods(self):
        products_ids = self.cart.keys()

        products = Product.objects.filter(id__in=products_ids)

        return products

    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)
        ourcart = self.cart
        # udpate Dictionary
        ourcart[product_id] = product_qty

        self.session.modified = True
        thing = self.cart
        return thing

    def delete(self, product):
        product_id = str(product)
        # value Delete from Dictionary
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

    def cart_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart
        total = 0
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * int(value))

                    else:
                        total = total + (product.price * int(value))


        return total