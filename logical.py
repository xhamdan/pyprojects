#The logical and
x = 10
y = 20 
z = 30 
if x > y and y > z:
    print('x is the greatest number')
else:
    print('x is not the greatest number')

#The logical or
x = 30
y = 50
z = 10
if x > y or x > z:
        print('x is atleast larger than one number.')
else: 
        print('x is the smallest number.')


#when usernames are provided.
username = 's'
password = 'sammy2'
if username == 'sam' and password == 'sammy20':
      print('you are logged in')
elif username =='sam' and password !='sammy20':
      print('Correct username , invalid password')
else: 
      print('invalid credentials.')
print('Conguratulations')

