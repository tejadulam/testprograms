# find the faculty with highest student count who got more  than 90%
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
more = {}
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
        
    more['Telugu'] = Telugu
    more["English"] = English
    more['Maths'] = Maths
    more['Pysics'] = Physics
    more["Chemistry"] = Chemistry
    more["Social"] = Social


print(more)
max_subject = max(more.items(),key=lambda x:x[1])
print("Highest Student count: ", max_subject)
a = max_subject
(sub,score) = a
print(faculty[sub])






# ------------- using list ------------------------
import csv
faculty = {
    'Telugu': 'Amarnath',
    'English': 'Samuel',
    'Maths': 'Murali Krishna',
    'Physics': 'Raja Gopal',
    'Chemistry': 'Ravi',
    'Social': 'Krishna Reddy'
}

subject_names = list(faculty.keys())
subject_counts = [0] * len(subject_names)

with open('C:/Users/teju2/Desktop/workstation/testprograms/Assignments1/student_marks.csv', 'r') as file:
    data = csv.DictReader(file)
    for record in data:
        for i, subject in enumerate(subject_names):
            if int(record[subject]) >= 90:
                subject_counts[i] += 1
max_count = max(subject_counts)
max_subject_index = subject_counts.index(max_count)
max_subject_name = subject_names[max_subject_index]

print("Subject with the highest student count who scored more than 90%:", max_subject_name)
print("Faculty handling that subject:", faculty[max_subject_name])



