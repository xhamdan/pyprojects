#Compute total,average & grade(basing on average scores) given scores from subjects
#def total_score(math,eng,sci,sst):
def compute_total(scores): #we use loops to iterate through
    total = 0
    for score in scores:
        total+=score
    
    return total
def compute_average(scores):
    number_of_items = len(scores)
    sum = compute_total(scores)
    average = sum / number_of_items

    return average

def get_grade(average):
    grade =""
    if average >=80:
        grade = "D1"
    elif average >=70:
        grade = "D2"
    elif average >=60:
        grade = "C3"
    elif average >=50:
        grade = "C4"
    else:
        grade = "F9"
    
    return grade





student_scores = [65,75,85,95]
print(f" The total scores for hamdan is: {compute_total(student_scores)}")
print(f" The average of the given scores is: {compute_average(student_scores)}")