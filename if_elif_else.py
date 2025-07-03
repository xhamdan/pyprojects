#if elif else: Used to make decision btn more than 2 alternatives.
#if i have x, i need to check when x is 5, or less, or greater.
x = 10
if x == 5:
    print("x is equal to 5")
elif x < 5:
    print('x is less than 5')
else:
    print('x is greater than 5')
print('Conguratulations, Done.')

#Example 2: WAP to check no is divisible by 2 or 3
n = 22
if n%2==0: 
    print('number is divisible by 2')
    print('You are are a genius')
elif n%3==0: 
    print('number is divisible by 3')
else: 
    print('no. is neither divisible by 2 nor 3')
print('Done.')

#More-Examples.
birth_year =int(input("Enter year of birth: "))
current_year =2025
age = current_year - birth_year
print(f'You are {age} years old')
if birth_year > current_year:
    print('Invalid entry')
elif age >=0 and age <=3:
    print('You are a baby')
elif age <=10: 
    print('You are a kid')
elif age<=20:
    print('You are a teenager')
elif age<=35:
    print('You are a youth')
elif age <=50: 
    print('You are an adult')
elif age >50:
    print('You are a senior citizen')
print('Conguratulations')