from alarm_clock import Alarm_clock
from product import Product
from shopping_cart import Shopping_Cart
from customer import Customer

first_alarm = Alarm_clock()
first_alarm.set_current_time()
first_alarm.set_alarm_on()
first_alarm.set_alarm_time()

final_cart = Shopping_Cart()

first_customer = Customer(final_cart, 'Arturo')
print(first_customer.customer_name)
first_product = Product("tomato", 4, 'vegetable')
second_product = Product("corn", 2, "vegetable")
third_product = Product("Pasta", 10, "noodle")
first_customer.add_new_product(first_product)
first_customer.add_new_product(second_product)
first_customer.add_new_product(third_product)
first_customer.view_products()
total_first_customer = first_customer.shopping_cart.calculate_total()
print(f"Total for cart is {total_first_customer}")
first_customer.shopping_cart.clear_cart()
first_customer.view_products()