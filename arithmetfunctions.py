def sum(number_1, number_2):
    total = number_1 + number_2

    return(total)
def subtraction (num_1, num_2):
    difference = num_1 - num_2 

    return(difference)

def multiplication (num_1, num_2): 
    product = num_1 * num_2

    return(product)

def division(num_1, numb2):
    quotent = num_1 /numb2

    return(quotent)

sum_results =sum(10,30)
sub_results=subtraction(14,20)
quo_results = division(40,10)

def average(num1,num2):
    compute_av = sum(num1,num2)
    average = compute_av/2

    return average



print(f"The Sum of the numbers is {sum_results}")
print(f" The difference is {sub_results}")
print(f"The quotient is {quo_results}")
