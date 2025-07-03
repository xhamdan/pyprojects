students_test_scores = [
    [40,80,90,64],
    [14,80,62,79],
    [52,92,88,96],
    [61,44,25,100]
    
    ]
count =1

for student in students_test_scores:
    print(f"student {count} Scores")
    test_total = 0
    for score in student:
        test_total+=score
    count+=1
    print(test_total)
