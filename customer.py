from shopping_cart import Shopping_Cart
class Customer():
    def __init__(self, Shopping_Cart ,name):
        self.customer_name = name
        self.shopping_cart = Shopping_Cart

    def add_new_product(self, product):
        self.shopping_cart.add_to_cart(product)
    
    def view_products(self):
        if len(self.shopping_cart.cart_products) == 0:
            print('Shopping Cart is empty')
        for index in range(len(self.shopping_cart.cart_products)):
            print(self.shopping_cart.cart_products[index].products_name)
