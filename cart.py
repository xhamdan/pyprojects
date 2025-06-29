foods =[]
prices =[]
total = 0

while True:
    #Ask users what food they need to buy
    food = input("Enter a food to buy ('Q to quit'): ")
    if food.lower() == 'q':
        break
    else:
        #We also need the user to enter the price. Lets ask the user to enter price.
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        #lets also append prices to prices
        prices.append(price)

print("-----------MEGA STARDAND SUPERMART---------------")
print("*" * 50)
for food in foods:
    #,end=" " aligns the foods to horizontol
    print(food,end=',')
for price in prices:
    total+=price

print(f" Your total is:$ {total}: $")