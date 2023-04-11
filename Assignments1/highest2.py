
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

            

# cols = ['studentname', 'Telugu', 'English', 'Maths', 'Physics', 'Chemistry', 'Social']
# rows = [['student1', '50', '40', '49', '81', '41', '72'],['student2', '37', '44', '95', '72', '33', '22'],['student3', '76', '39', '97', '96', '61', '57'],['student4', '56', '85', '67', '87', '21', '62'],['student5', '81', '85', '73', '69', '40', '47'],['student6', '64', '38', '15', '38', '84', '39'],['student7', '88', '65', '26', '36', '39', '95'],['student8', '43', '53', '38', '83', '99', '35'],['student9', '45', '84', '92', '96', '26', '52'],['student10', '61', '65', '23', '32', '62', '20'],['student11', '54', '21', '65', '50', '18', '72'],['student12', '90', '65', '26', '69', '38', '95'],['student13', '23', '45', '47', '70', '60', '42'],['student14', '40', '31', '19', '74', '73', '66'],['student15', '22', '69', '48', '95', '26', '26'],['student16', '62', '26', '41', '23', '52', '95'],['student17', '60', '71', '37', '60', '58', '15'],['student18', '87', '92', '77', '98', '96', '71'],['student19', '81', '87', '18', '21', '94', '67'],['student20', '32', '98', '36', '19', '87', '68'],['student21', '62', '54', '72', '60', '31', '71'],['student22', '93', '66', '16', '47', '60', '18'],['student23', '67', '28', '76', '56', '49', '43'],['student24', '59', '65', '56', '32', '48', '95'],['student25', '43', '50', '39', '27', '56', '87'],['student26', '46', '75', '93', '84', '94', '86'],['student27', '37', '27', '72', '48', '28', '53'],['student28', '95', '56', '52', '34', '46', '15'],['student29', '91', '25', '50', '81', '35', '16'],['student30', '84', '85', '47', '78', '16', '39'],['student31', '58', '65', '94', '54', '98', '17'],['student32', '81', '58', '74', '35', '33', '61'],['student33', '71', '43', '69', '78', '85', '56'],['student34', '87', '77', '77', '65', '49', '44'],['student35', '59', '51', '33', '49', '17', '52'],['student36', '56', '29', '71', '59', '82', '38'],['student37', '92', '29', '15', '64', '74', '33'],['student38', '51', '44', '68', '65', '21', '39'],['student39', '49', '83', '46', '36', '35', '57'],['student40', '60', '94', '99', '59', '48', '98'],['student41', '89', '72', '83', '75', '54', '66'],['student42', '26', '86', '69', '48', '35', '19'],['student43', '21', '67', '64', '45', '28', '49'],['student44', '68', '55', '80', '62', '38', '33'],['student45', '84', '95', '63', '21', '63', '57'],['student46', '40', '93', '41', '21', '74', '65'],['student47', '58', '23', '77', '84', '80', '81'],['student48', '38', '17', '97', '51', '40', '80'],['student49', '42', '78', '27', '38', '29', '90'],['student50', '88', '32', '42', '17', '69', '75'],['student51', '69', '94', '62', '79', '42', '73'],['student52', '100', '99', '19', '52', '35', '88'],['student53', '87', '65', '60', '36', '39', '75'],['student54', '94', '55', '66', '90', '40', '38'],['student55', '79', '32', '23', '54', '22', '79'],['student56', '60', '29', '74', '97', '84', '95'],['student57', '73', '24', '69', '70', '72', '79'],['student58', '41', '87', '67', '31', '58', '57'],['student59', '63', '62', '23', '25', '34', '35'],['student60', '85', '74', '98', '83', '81', '15']]

# with open('student_marks.csv','w') as file:
#     data = csv.writer(file)
#     data.writerow(cols)
#     data.writerows(rows)
import csv

Telugu = 0
English = 0
Maths = 0
Physics = 0
Chemistry = 0
Social = 0

sub_faculty = {
    'Maths' : 'Murali Krishna',
    'Telugu' : 'Amarnath',
    'English' : 'Samuel',
    'Social' : 'Krishna Reddy',
    'Physics' : 'Raja Gopal',
    'Chemistry' : 'Ravi'
}

hpass_mark = {}

with open('C:/Users/teju2/Desktop/workstation/testprograms/Assignments1/student_marks.csv','r') as csvfile:
    data = csv.DictReader(csvfile)
    for marks in data:
        if int(marks['Telugu']) > 40:
            Telugu += 1
        if int(marks['English']) > 40:
            English += 1
        if int(marks['Maths']) > 40:
            Maths += 1
        if int(marks['Physics']) > 40:
            Physics += 1
        if int(marks['Chemistry']) > 40:
            Chemistry += 1
        if int(marks['Social']) > 40:
            Social += 1
    hpass_mark['Telugu'] = Telugu
    hpass_mark['English'] = English
    hpass_mark['Maths'] = Maths
    hpass_mark['Physics'] = Physics
    hpass_mark['Chemistry'] = Chemistry
    hpass_mark['Social'] = Social

print(hpass_mark)
pass_perc = max(hpass_mark.items(),key=lambda x:x[1])
print(f"Highest Pass Percentage is {pass_perc}")
faculty = (pass_perc); (sub,marks) = faculty
print(pass_perc)
print(sub_faculty[sub])