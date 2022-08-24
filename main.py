from alarm_clock import Alarm_clock
from product import Product
from shopping_cart import Shopping_Cart
from customer import Customer

first_alarm = Alarm_clock()
first_alarm.set_current_time()
first_alarm.set_alarm_on()
first_alarm.set_alarm_time()

first_product = Product("tomato", 4, 'vegetable')
final_cart = Shopping_Cart(first_product)
final_cart.calculate_total(first_product)

first_customer = Customer(final_cart, 'Arturo')
second_product = Product("corn", 2, "vegetable")
first_customer.add_new_product(second_product)
first_customer.view_products()