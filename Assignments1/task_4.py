# 4. Who is the top student with maximum total?
import csv

def top_student_max_total(student_marks):
    with open(student_marks,'r') as csvfile:
        data = csv.DictReader(csvfile)
        total_marks = {}
        for records in data:
            marks = (int(records['Telugu']), int(records['English']), int(records['Maths']), int(records['Physics']), 
                    int(records['Chemistry']), int(records['Social']))
            total = sum(marks)
            total_marks[records['studentname']] = total
        students = sorted(total_marks.items(), key=lambda x: x[1], reverse=True)
        msg4 = f"The Top Student is {students[0][0]} and his top mark is {students[0][1]}"

    return msg4

print(top_student_max_total('Assignments1/student_marks.csv'))

# print(f"The Top Student is {students[0][0]} and his top mark is {students[0][1]}")