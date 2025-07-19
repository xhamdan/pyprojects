def sum_list(student_scores):
    total =0
    for score in student_scores:
        total+=score

    return(total)

scores = [65,58,75,80,60,100,90,68,90,300]
results = sum_list(scores)
print(results)