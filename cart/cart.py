from products.models import Products


class Cart:
    def __init__(self, request):
        """"
        Initialize the cart
        """
        self.request = request

        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def __iter__(self):
        """
        iteration for products in the cart
        """
        products = self.get_products()

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product

        for item in cart.keys():
            yield item

    def __len__(self):
        """"
        Return the length of products in the cart
        """
        return len(self.cart.keys())

    def get_products(self):
        """"
        Return the information of products from database which are in the cart
        """
        products_ids = self.cart.keys()
        return Products.objects.filter(id__in=products_ids)

    def add(self, product, quantity=1):
        """"
        Add the specified product to cart
        """
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity}
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def remove(self, product):
        """"
        Remove the specified product from the cart
        """
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        """"
        Clear the Cart
        """
        del self.session['cart']
        self.save()

    def get_total_price(self):
        """"
        Return the total price of all products in the cart
        """
        total_price = 0

        for product in self.__iter__():
            total_price += product['quantity'] * product['product_obj'].price()
        return total_price

    def save(self):
        """"
        Save the cart changes to the session
        """
        self.session.modified = True
