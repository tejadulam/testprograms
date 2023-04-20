# 7. Find the student with least numbers of marks as total.
import csv

def student_least_marks_totla(student_marks):
    with open(student_marks,'r') as csvfile:
        data = csv.DictReader(csvfile)
        total_marks = {}
        for records in data:
            marks = (int(records['Telugu']), int(records['English']), int(records['Maths']), int(records['Physics']), 
                    int(records['Chemistry']), int(records['Social']))
            total = sum(marks)
            total_marks[records['studentname']] = total
        students = sorted(total_marks.items(), key=lambda x: x[1])
        msg7 = f"The Student is {students[0][0]} and his Least mark is {students[0][1]}"
    
    return msg7
print(student_least_marks_totla('Assignments1/student_marks.csv'))