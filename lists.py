students_names = []
list2 = ['Juma','Joy','Peter']
#students_names.insert(2,list2)
#students_names.append('hamid')
#print(students_names.count('hamdan')) 2 times
#This programm below appends new applicants to student names list above
while True:
     name=input("enter student name: " )
     if name =='q':
          break
     else: 
          students_names.append(name)

for student in students_names:
    print(student)