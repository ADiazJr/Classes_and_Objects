from product import Product
class Shopping_Cart():
    def __init__(self):
        self.cart_products = []

    def calculate_total(self):
        cart_total = 0
        for index in range(len(self.cart_products)):
            cart_total += self.cart_products[index].price
        return cart_total

    def add_to_cart(self, products):
        self.cart_products.append(products)

    def clear_cart(self):
        while len(self.cart_products) != 0:
            self.cart_products.pop(0)
