# who is the best student in maths

import csv

def top_student_max_subject(student_marks, subject):
    with open(student_marks, 'r') as csvfile:
        data = csv.DictReader(csvfile)
        subject_marks = {}
        for records in data:
            marks = int(records[subject])
            subject_marks[records['studentname']] = marks
        students = sorted(subject_marks.items(), key=lambda x: x[1], reverse=True)
        msg = f"The top student in {subject} is {students[0][0]} with a score of {students[0][1]}"

    return msg

print(top_student_max_subject('Assignments1/student_marks.csv', 'Maths'))