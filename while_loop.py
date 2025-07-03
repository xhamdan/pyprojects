#Print numbers and get their sum
counter = 2
sum = 0
while counter <= 5: 
    number =int(input(f'Enter {counter}: '))
    sum = sum + number
    counter += 1
print(f'\nsum: {sum}')
    
print(f'Conguratulations - You have added your {counter} numbers')