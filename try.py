username = "hamid."
password = "geek"
if username !="hamid" and password =="geek":
    print('Invalid credentials')
else:
    print("you are right")

p = "female"
q = "male"
print(f'All Ugandans who are {p} \nor {q} are fools')

birth_year=input("Enter birth year::")
current_year = 2025
age = current_year - int(birth_year)
if age >30: 
    print(f'Your {age} is for an adult')
else: 
    print('You are still sexy')

#Registration number: 
print(f' your regno is: {username[:4]}{age}')