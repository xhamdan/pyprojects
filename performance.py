students = ['hamdan','Naluwooza']
subjects = ['data analytics','ICT 4 Org','introductory arabic','Business PM']
#These 2 variables to track no. of passes and failures
pass_count = 0 
fail_count = 0
#Now create a loop to iterate through the marks of the students
average_pass_mark = float(input('Enter average pass mark: '))
number_of_subjects = int(input("Enter number of subjects: "))

for student in students: 
    print(f"\t{student.upper()} Scores")
    student_total = 0 # Since it is going to be computed

    for subject in subjects:
        subject_score = int(input(f"\tEnter {subject.upper()} score: "))
       # if (len(subject_score))>100:
            
        student_total +=subject_score
        student_average = student_total/(number_of_subjects)
if student_average >= average_pass_mark:
        pass_count+=1
else: 
        fail_count+=1
print(f"Total Passed:{pass_count}\nTotal Failed: {fail_count}")