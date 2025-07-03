#Dictionaries contain items that are mutable
employee = {
    'name':'Kasule',
    'dept':'CIT',
    'pay' : 200000,
    'sex' : 'Male'
}
mystuff = {
    'apple':'i am apples'
}

student_marks = {'sara':99,
                 'anesa':100,
                 'tom' :50

}

student_marks.update({'hamid':80, #This line adds multiple key/value pairs to a dict
                      'halimah':34,
                      'fred':56})
student_marks['hamdan'] = 85 # This adds student 'hamdan' with his mark of 85 to the dict ->student-marks
employee['pay']=350000
for key in student_marks: #views are iterable.
    print(key)


#print(employee.items())
#print(mystuff['apple'])

print(f"hamdan scored: {student_marks.get('hamdan',0)}")
#print(len(student_marks))

print(employee.items())
#print(employee.clear())


