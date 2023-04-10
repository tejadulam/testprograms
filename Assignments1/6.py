# --- average marks for each subject

import csv

with open('C:/Users/teju2/Desktop/workstation/testprograms/Assignments1/student_marks.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    total_marks = {}
    for row in reader:
        marks = (int(row['Telugu']), int(row['English']), int(row['Maths']), int(row['Physics']), int(row['Chemistry']), int(row['Social']))
        total = sum(marks)
        total_marks[row['studentname']] = total
    students = sorted(total_marks.items(), key=lambda x: x[1], reverse=True)
print(f"The Top Student is {students[0][0]} and his top mark is {students[0][1]}")



import csv

telugu_sum = 0; telugu_count = 0
english_sum = 0; english_count = 0
maths_sum = 0; maths_count = 0
physics_sum = 0; physics_count = 0
chemistry_sum = 0; chemistry_count = 0
social_sum = 0; social_count = 0

pass_mark = 40

avg_marks = {}

with open('student_marks.csv','r') as csvfile:
    data = csv.DictReader(csvfile)
    for record in data:
        if int(record['Telugu']) >= pass_mark:
            telugu_sum += int(record['Telugu'])
            telugu_count += 1
        if int(record['English']) >= pass_mark:
            english_sum += int(record['English'])
            english_count += 1
        if int(record['Maths']) >= pass_mark:
            maths_sum += int(record['Maths'])
            maths_count += 1
        if int(record['Physics']) >= pass_mark:
            physics_sum += int(record['Physics'])
            physics_count += 1
        if int(record['Chemistry']) >= pass_mark:
            chemistry_sum += int(record['Chemistry'])
            chemistry_count += 1
        if int(record['Social']) >= pass_mark:
            social_sum += int(record['Social'])
            social_count += 1

    avg_marks['Telugu'] = telugu_sum/telugu_count
    avg_marks['English'] = english_sum/english_count
    avg_marks['Maths'] = maths_sum/maths_count
    avg_marks['Physics'] = physics_sum/physics_count
    avg_marks['Chemistry'] = chemistry_sum/chemistry_count
    avg_marks['Social'] = social_sum/social_count

Subjects = sorted(avg_marks.items(),key = lambda x: x[1],reverse=True)
print(Subjects)
print(f"Ignoring failures,the Average mark for {Subjects[0][0]} is {round(Subjects[0][1])}")
print(f"Ignoring failures,the Average mark for {Subjects[1][0]} is {round(Subjects[1][1])}")
print(f"Ignoring failures, the Average mark for {Subjects[2][0]} is {round(Subjects[2][1])}")
print(f"Ignoring failures,the Average mark for {Subjects[3][0]} is {round(Subjects[3][1])}")
print(f"Ignoring failures, the Average mark for {Subjects[4][0]} is {round(Subjects[4][1])}")
print(f"Ignoring failures,the Average mark for {Subjects[5][0]} is {round(Subjects[5][1])}")


