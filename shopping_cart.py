#Organising a shopping cart
print("\===Ham Shopping Mall===")
print("""
1. Bread\t\t 2500/-
2. Sugar\t\t 3500/-
3. C-Oil\t\t 1500/-
4. Soap\t\t\t 1000/-
      """)
item_code =int(input('Item Code: '))
item_quantity =int(input('Item Quantity: '))
item_price = 0
discount = 0
item_name = ''
amount_paid = 0

if item_code==1:
    item_name = 'Bread'
    item_price = item_quantity * 2500

elif item_code==2:
    item_name = 'Sugar'
    item_price = item_quantity * 3500
    discount = 0.5 * item_price
    if item_quantity > 200:
        amount_paid = item_price - discount
    else:
        discount = 0
elif item_code==3:
    item_name = 'c-oil'
    amount_paid = item_quantity * 1500
elif item_code ==4:
    item_name = 'soap'
    amount_paid = item_quantity * 1000
else: 
    print('Undefined Item')
print(f' \nItem Quantity: {item_quantity} \nItem Name: {item_name} \nTotal price: {item_price} shillings \n Discount: {discount} \namount_paid: {amount_paid}')