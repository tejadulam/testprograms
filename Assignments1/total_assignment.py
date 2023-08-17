import csv

Telugu = 0
English = 0
Maths = 0
Physics = 0
Chemistry = 0
Social = 0

faculty = {
    'Telugu' : 'Amarnath',
    'English' : 'Samuel',
    'Maths' : 'Murali Krishna',
    'Physics' : 'Raja Gopal',
    'Chemistry' : 'Ravi',
    'Social' : 'Krishna Reddy'
}

sub_faculty = {}

with open('C:/Users/teju2/Desktop/workstation/testprograms/Assignments1/student_marks.csv','r') as file:
    data = csv.DictReader(file)
    for record in data:
        if int(record['Telugu']) >= 90:
            Telugu+=1
        if int(record['English']) >= 90:
            English+=1
        if int(record["Maths"]) >= 90:
            Maths+=1
        if int(record["Physics"]) >= 90:
            Physics+=1
        if int(record["Chemistry"]) >= 90:
            Chemistry+=1
        if int(record["Social"]) >= 90:
            Social+=1
        
    sub_faculty['Telugu'] = Telugu
    sub_faculty["English"] = English
    sub_faculty['Maths'] = Maths
    sub_faculty['Physics'] = Physics
    sub_faculty["Chemistry"] = Chemistry
    sub_faculty["Social"] = Social


# find the faculty with highest student count who got more than 90%
m = max(sub_faculty, key= sub_faculty.setdefault)
print(f"The faculty with the most high scores is {faculty[m]} with {sub_faculty[m]} students who scored more than 90%.")

# find the faculty with highest pass percentage(>40)
with open('C:/Users/teju2/Desktop/workstation/testprograms/Assignments1/student_marks.csv','r') as file:
    data = csv.DictReader(file)
    for record in data:
        if int(record['Telugu']) > 40:
            Telugu+=1
        if int(record['English']) > 40:
            English+=1
        if int(record["Maths"]) > 40:
            Maths+=1
        if int(record["Physics"]) > 40:
            Physics+=1
        if int(record["Chemistry"]) > 40:
            Chemistry+=1
        if int(record["Social"]) > 40:
            Social+=1
        
    sub_faculty['Telugu'] = Telugu
    sub_faculty["English"] = English
    sub_faculty['Maths'] = Maths
    sub_faculty['Physics'] = Physics
    sub_faculty["Chemistry"] = Chemistry
    sub_faculty["Social"] = Social

n = max(sub_faculty, key = sub_faculty.setdefault)
pass_percentage = ((sub_faculty[n]/(123)*(100)))
print(f"The faculty with the most high scores is {faculty[n]} with {pass_percentage} students who scored more than 40%.")

# find the faculty with least pass percentage(<=40)
with open('C:/Users/teju2/Desktop/workstation/testprograms/Assignments1/student_marks.csv','r') as file:
    data = csv.DictReader(file)
    for record in data:
        if int(record['Telugu']) <= 40:
            Telugu+=1
        if int(record['English']) <= 40:
            English+=1
        if int(record["Maths"]) <= 40:
            Maths+=1
        if int(record["Physics"]) <= 40:
            Physics+=1
        if int(record["Chemistry"]) <= 40:
            Chemistry+=1
        if int(record["Social"]) <= 40:
            Social+=1
        
    sub_faculty['Telugu'] = Telugu
    sub_faculty["English"] = English
    sub_faculty['Maths'] = Maths
    sub_faculty['Physics'] = Physics
    sub_faculty["Chemistry"] = Chemistry
    sub_faculty["Social"] = Social

v = min(sub_faculty, key = sub_faculty.setdefault)
least_pass_percentage = ((sub_faculty[v]/(123)*(100)))

print(f"The faculty with the most high scores is {faculty[v]} with {least_pass_percentage} students who scored less than and equal than 40%.")

# who is the top student with maximum total

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

# who is the best student in mathematics:


import csv

Telugu = 0
English = 0
Maths = 0
Physics = 0
Chemistry = 0
Social = 0

faculty = {
    'Telugu' : 'Amarnath',
    'English' : 'Samuel',
    'Maths' : 'Murali Krishna',
    'Physics' : 'Raja Gopal',
    'Chemistry' : 'Ravi',
    'Social' : 'Krishna Reddy'
}

best_student_mathematics = ''
highest_marks_mathematics = 0

with open('C:/Users/teju2/Desktop/workstation/testprograms/Assignments1/student_marks.csv','r') as file:
    data = csv.DictReader(file)
    for record in data:
        if int(record['Maths']) >= 90:
            Maths += 1
            if int(record['Maths']) > highest_marks_mathematics:
                highest_marks_mathematics = int(record['Maths'])
                best_student_mathematics = record['studentname']
        if int(record['Telugu']) >= 90:
            Telugu += 1
        if int(record['English']) >= 90:
            English += 1
        if int(record["Physics"]) >= 90:
            Physics += 1
        if int(record["Chemistry"]) >= 90:
            Chemistry += 1
        if int(record["Social"]) >= 90:
            Social += 1
        
    sub_faculty = {
        'Telugu': Telugu,
        'English': English,
        'Maths': Maths,
        'Physics': Physics,
        'Chemistry': Chemistry,
        'Social': Social
    }

print("Best student in Mathematics: ", best_student_mathematics, "with marks:", highest_marks_mathematics)



# what is the average marks for each sub(ignore failures)

import csv

telugu_sum = 0; telugu_count = 0
english_sum = 0; english_count = 0
maths_sum = 0; maths_count = 0
physics_sum = 0; physics_count = 0
chemistry_sum = 0; chemistry_count = 0
social_sum = 0; social_count = 0

pass_mark = 40

avg_marks = {}

with open('C:/Users/teju2/Desktop/workstation/testprograms/Assignments1/student_marks.csv','r') as csvfile:
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


# find the student withleast number of marks as total

import csv
with open('C:/Users/teju2/Desktop/workstation/testprograms/Assignments1/student_marks.csv') as csvfile:
    data = csv.DictReader(csvfile)
    total_marks = {}
    for records in data:
        marks = (int(records['Telugu']), int(records['English']), int(records['Maths']), int(records['Physics']), 
                 int(records['Chemistry']), int(records['Social']))
        total = sum(marks)
        total_marks[records['studentname']] = total
    students = sorted(total_marks.items(), key=lambda x: x[1])
print(f"The Student is {students[0][0]} and his Least mark is {students[0][1]}")
