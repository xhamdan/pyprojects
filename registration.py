#A program to register users with their passwords.
from os import system
username = input('Enter username: ')
password = input('Enter password: ')
confirm_password =input('confirm_password: ')
if len(password) > 10:
    print('Password should not exceed 10 characteristd')
elif len(password) < 6: 
    print('Password should contain atleast 6 characters')
else:
    #system('cls')
    if password ==confirm_password:
        print('Password created successfully')
    else:
        print('Passwords do not match')