#Make use of the date-time library by importing it
import datetime
import math
#store some information (Store name, address, cashiers details)
store_name ="mega standard supermarket"
store_address="Plot 10, Kibuli Hill"
cashier_name = "Mbonye Fred"
store_telnumber= '+256414(0)-674-315'

#now = datetime.datetime.now
#date_time = datetime.now.strftime("%Y-M-D %H:%M:%S")

#product names and prices
p1_name,p1_price = "Sugar",1000
p2_name,p2_price = "cooking-oil",1000
p3_name,p3_price = "Bread",2000

items_sold = 3
#calculate the subtotal
subtotal = p1_price + p2_price + p3_price
#calculate the tax
food_tax = (subtotal * 0.18)
#grand total
grandTotal = subtotal + food_tax

#message
return_message = "No return for Milk, Products and Meats"
apprec_message = "Thank you for your business"

#report - output
print(f"\t\t\t\t{store_name.title()} \n\t\t\t\t{store_address} \n\t\t\t\t{store_telnumber}")
print(f"\t\t\t\tCashier: {cashier_name}")

print("*" * 80)
print("\t\t\t\tGROCERY")
print(f"\t\t\t\t{p1_name}\t\t{p1_price}")
print(f"\t\t\t\t{p2_name}\t{p2_price}")
print(f"\t\t\t\t{p3_name}\t\t{p3_price}")



