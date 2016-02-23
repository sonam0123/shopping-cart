class Cart(object):
    """cart.
    cart =  [
        {
            'id': 1,
            'name': 'Name of Product',
            'image': '/path/to/image/,
            'quantity': 2,
        },
        {
            ...
            ...
        }
    ]
    request.sesison['cart'] = cart

    exhisting_cart = request.session['cart']
    # adding an item
    exhisting_cart.append({'id': 1, 'name': '})

    # deleting: id = 2
    for item in exhisting_cart:
        if item['id'] == 2:
            item.remove(item)

    # updateing
    for item in exhisting_cart:
        if item['id'] == 2:
            item['quantity'] -= 1

    """

    def __init__(self, request, *args, **kwargs):
        self.request = request
        return super(Cart, self).__init__(*args, **kwargs)

    def get_cart(self):
        cart = self.request.session.get('cart', [])
        if not len(cart):
            self.request.session['cart'] = []
        return cart

    def add_item(self, product, quantity=1):
        """Add item to cart
        """
        cart = self.get_cart()
        for item in cart:
            if item['id'] == product.id:
                item['quantity'] += quantity
                item['price'] = (product.price * item['quantity']),
                self.request.session['cart'] = cart
                return cart
        item = {
            'id': product.id,
            'name': product.name,
            'image': product.image.url,
            'quantity': quantity,
            'price': (product.price * quantity),
        }
        cart.append(item)
        self.request.session['cart'] = cart
        return cart

    def delete_item(self, product):
        """Delete item from cart."""
        cart = self.get_cart()
        for item in cart:
            if item['id'] == product.id:
                cart.remove(item)
        self.request.session['cart'] = cart
        return cart

    # def increase_item_quantity(self, product, increase_by=1):
    #     """Increase items quantity by `increase_by`. """
    #     cart = self.get_cart()
    #     for item in cart:
    #         if item['id'] == product.id:
    #             item['quantity'] += increase_by
    #             self.request.session['cart'] = cart
    #     return cart
    #
    # def decrease_item_quantity(self, product, decrease_by=1):
    #     """Increase items quantity by `increase_by`. """
    #     cart = self.get_cart()
    #     for item in cart:
    #         if item['id'] == product.id:
    #             item['quantity'] -= decrease_by
    #             self.request.session['cart'] = cart
    #     return cart

    def discard_cart(self):
        self.request.session.pop('cart', None)
        return True
