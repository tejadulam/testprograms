
# find the faculty with highest student count who got more  than 90%
import csv
def fac_with_high_studentcount(students_marks_csv,faculty_csv):
    Telugu = 0
    English = 0
    Maths = 0
    Physics = 0
    Chemistry = 0
    Social = 0
    high_marks = {}
    msg = None
    with open(students_marks_csv,'r') as csvfile:
        data = csv.DictReader(csvfile)
        for record in list(data):
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
                Social += 1
        high_marks['Telugu'] = Telugu
        high_marks["English"] = English
        high_marks['Maths'] = Maths
        high_marks['Pysics'] = Physics
        high_marks["Chemistry"] = Chemistry
        high_marks["Social"] = Social

    max_marks = max(high_marks.items(),key=lambda x: x[1])
    print(max_marks)
    with open(faculty_csv,"r") as csvfile:
        faculty_data = list(csv.DictReader(csvfile))
        for i in faculty_data:
            if max_marks[0] == i["Subject"]:
                msg = f'The faculty with highest student count who got more than 90 percent is {i.get("Faculty")} and his subject is {i.get("Subject")}'
                print(i)
    return msg
print(fac_with_high_studentcount('C:/Users/teju2/Desktop/workstation/testprograms/Assignments1/student_marks.csv', 'C:/Users/teju2/Desktop/workstation/testprograms/Assignments1/subject_faculty.csv'))


