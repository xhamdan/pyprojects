cgpa = float(input('Enter CGPA: '))
gender =input('Enter students gender: ')
award =''
cgpa_class = 'N/A'
if cgpa <= 1.9:
    cgpa_class ="Fail"
elif cgpa<= 2.4:
    cgpa_class = "Pass"
elif cgpa<= 3.5:
    cgpa_class = "Second Lower"
elif cgpa_class<= 4.4:
    cgpa_class ="Second Upper"
elif cgpa<= 5.0:
    cgpa_class = "First Class"
    if gender =='male':
        award ='Gold'
    elif gender =='female':
        award ='Gold and a Laptop'
else:
    print('Invalid CGPA Entry')
print(f'Your CGPA is: {cgpa}\n And your degree class is: {cgpa_class}')