#We need to compute students scores in a primary school
subjects =['MAT', 'SST','SCI','ENG']
students =[] # We shall append to this list anytime we add new students
student_scores = [] # This will be a multi-dimensional list
no_of_students = int(input("Enter No. of students: "))
#You can use the while or for loop

for number in range(no_of_students):
    student =input("Enter Student Name: ")
    #for each student added we now need to append/add them to the list of students, students=[]
    students.append(student)
    #Lets now see/create a list for the subject scores for each subjects
    subject_scores = []
    #total = 0
    for subject in subjects:
        #create a variable i.e. score to store the score obtained in each subject.
        
        score =int(input(f'\tEnter {student}||{subject} score: '))
        subject_scores.append(score)
    student_scores.append(subject_scores)

    #output - Organise the marks in a tabular view.
print("\n\tStudent \tMAT \tSST \tSCI \tENG \tTotal \tAverage")
index = 0
for student in student_scores:
    output  = f"\t{students[index]}\t"
    total = 0
    average = 0
    for score in student:
        output+=f"\t{score}"
        total+=score
        average = total/len(subjects)
    
    index+=1
    print(f"{output} \t{total}\t{average}")


#print(students)
#print(student_scores) # This contains all student scores
