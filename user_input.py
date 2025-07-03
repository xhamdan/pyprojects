#User Input : Assume you have created a programme that captures users names
birth_year = input("Enter birth_year: ") #It is also better to tell user what this input is
fullname = input("Enter Fullname:")
current_year = 2021
age = current_year - int(birth_year)
print(f'Hello, {fullname} you are {age} years old')
