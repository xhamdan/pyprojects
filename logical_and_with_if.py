"""dob = int(input('Enter date of birth: '))
nationality=input('Enter nationality: ')
current_year = 2025
age = current_year - dob
if age > 18 and age < 30 and nationality =='Indian':
    print('You are eligible for the exam')
else:
    print('You are a foreigner')
print('Thank you for using Smart tech')"""

#Example 2:
dob = int(input("Enter date of birth: "))
nationality = input('Enter nationality: ')
current_year = 2025
age = current_year - dob
if age > 15 and age < 30 and nationality =='indian':
    print('You are eligible for exam. Exam fee is Rupee: 1500')
elif age > 15 and age < 30 and nationality =='american':
    print('You are eligible for the exam. Exam fee is $100')
else:
    print('Your country is not catered for')
print('End of program')

# Checking if a weekend
today = input("Enter day of the week: ")
if today =='sunday' or today =='saturday': 
    print('Its a weekend')
elif today =='monday' or today=='tuesday' or today=='wednesday' or today =='Thursday' or today=='friday':
    print('It is still a week day')
else: 
    print('undefined period')
print('End of program')