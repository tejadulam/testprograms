
# --student with least num of marks as total-----

import csv

with open('C:/Users/teju2/Desktop/workstation/testprograms/Assignments1/student_marks.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    total_marks = {}
    for row in reader:
        marks = (int(row['Telugu']), int(row['English']), int(row['Maths']), int(row['Physics']), int(row['Chemistry']), int(row['Social']))
        total = sum(marks)
        total_marks[row['studentname']] = total
    students = sorted(total_marks.items(), key=lambda x: x[1])
print(f"The Student {students[0][0]} with least mark is {students[0][1]}")