from os import system

secret_username = 'hamdan'
secret_password ='admin123'
login_attempts  = 0
login_limit     = 3
while login_attempts < login_limit:
    username = input('EnterUsername:  ')
    password = input('Enter password: ')
    if username and password:
        print(f'\nHello {username} Welcome to Stanbic Bank Uganda')
        #break; If correct credentials program will end here.
    else:
        system('cls') # clears display of -u & -p 
        print('Invalid credentials')
    login_attempts +=1
else:
    print('You have exceeded the login attempts')