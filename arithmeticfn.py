def sum():
    number_1 = int(input('Enter first number: '))
    number_2 = int(input('Enter second number: '))
    sum = number_1 + number_2
    print(sum)
sum()

#alternative way of computing sums
def sum2(no1,no2): 
    sum2 = no1+no2
    
    return sum2

sum2(10,100)
sum2(20,15)

#We may need to use the sums above in an activity below to find ----average.
results = sum2(20,10)
average = results/2

print(results)
print(average)
