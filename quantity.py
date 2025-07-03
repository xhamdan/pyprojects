#A program to compute items take by a customer in a supermarket
customer_name =input("Enter customername:")
item_p_name=input("Enter name of item_p picked:")
quantity_of_p=input("Enter Quantity of :")
price_of_item_p=input("Enter price of p:")
total_payment = int(quantity_of_p) * float(price_of_item_p)
print(f'Dear {customer_name}, your total payment for {item_p_name}s picked is {total_payment} UGX')