count = 0
student_test_scores = [
    [20,15,10],
    [30,25,5], 
    [15,21,12]
]

for student in student_test_scores: 
    print(f'Student {count} {student}')
    total_score = 0
    count+=1

    for score in student:
        total_score+=score
        
    print(f'Test Total {total_score}')