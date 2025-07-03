numbers ={
    '0' :'zero',
    '1' :'one',
    '2' :'two',
    '3' :'three',
    '4' :'four',
    '5' :'five',
    '6' :'six',
    '7' :'seven',
    '8' :'eight',
    '9' :'nine',
    }
user_number =input('Enter Number to Read: ')
output =''
for digit in user_number:
    output+=numbers.get(digit,'*') + " "
print(output)