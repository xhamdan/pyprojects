def greet(name,message):
    print(f"Hello {name}")
    print(message, disclaimer)

person = input("Enter Persons Name: ")
mesaj = input("Enter the message: ")
disclaimer = input('Provide disclaimer: ')

greet(person,mesaj,disclaimer)