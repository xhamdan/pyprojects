def sum(number_1, number_2):
    total = int(number_1) + int(number_2)

    return(total)
def subtraction (num_1, num_2):
    difference = int(num_1) - int(num_2)

    return(difference)

def multiplication (num_1, num_2): 
    product = int(num_1) * int(num_2)

    return(product)

def division(num_1, numb2):
    quotent = float(num_1) /float(numb2)

    return(quotent)

def average(num1,num2):
    compute_av = sum(num1,num2)
    average = float(compute_av)/2

    return average

value_1 = input("First Number: ")
value_2 = input("Second Number: ")

sum_results =sum(value_1,value_2)
av_results = average(value_1,value_2)


print(f"The Sum of the numbers is {sum_results}")
print(f" The average of the numbers is {av_results}")
