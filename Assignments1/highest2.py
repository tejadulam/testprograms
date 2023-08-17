
#  find the faclty with highest pass percentage
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
hpass_per = {}

with open('C:/Users/teju2/Desktop/workstation/testprograms/Assignments1/student_marks.csv','r') as file:
    data = csv.DictReader(file)
    for record in data:
        if int(record['Telugu']) <= 90 and int(record['Telugu']) >= 40:
            Telugu+=1
        if int(record['English']) <= 90 and int(record['English']) >= 40:
            English+=1
        if int(record["Maths"]) <= 90 and int(record['Maths']) >= 40:
            Maths+=1
        if int(record["Physics"]) <= 90 and int(record['Physics']) >= 40:
            Physics+=1
        if int(record["Chemistry"]) <= 90 and int(record['Chemistry']) >= 40:
            Chemistry+=1
        if int(record["Social"]) <= 90 and int(record['Social']) >= 40:
            Social+=1
        
    hpass_per['Telugu'] = Telugu
    hpass_per["English"] = English
    hpass_per['Maths'] = Maths
    hpass_per['Pysics'] = Physics
    hpass_per["Chemistry"] = Chemistry
    hpass_per["Social"] = Social


print(hpass_per)
max_subject = max(hpass_per.items(),key=lambda x:x[1])
print("Highest pass percentage: ", max_subject)
a = max_subject
(sub,score) = a
print("faculty name of the highest pass perc:",faculty[sub])

            

