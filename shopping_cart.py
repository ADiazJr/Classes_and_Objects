from product import Product
class Shopping_Cart():
    def __init__(self, products):
        self.cart_products = [products]

    def calculate_total(self, products):
        print(products.price)

    def add_to_cart(self, products):
        self.cart_products.append(products)

    def clear_cart(self):
        while len(self.cart_products) != 0:
            self.cart_products.remove()
