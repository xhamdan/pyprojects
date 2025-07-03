counter =1
total = 0
for numbers in range(5):
    users_number = int(input(f'Enter number {counter}: '))
    total+=users_number
    counter+=1
print(f'The Sum of the numbers entered is equal to: {total}')
