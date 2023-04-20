# ---  find the faclty with highest pass percentage
import csv

def highest_pass_percentage(student_marks_csv, faculty_details_csv):
    Telugu = 0
    English = 0
    Maths = 0
    Physics = 0
    Chemistry = 0
    Social = 0
    hpass_per = {}
    msg = None

    with open(student_marks_csv,'r') as csvfile:
        data = csv.DictReader(csvfile)
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

    max_marks = max(hpass_per.items(),key=lambda x: x[1])
    print(max_marks)
    with open(faculty_details_csv,"r") as csvfile:
        faculty_data = list(csv.DictReader(csvfile))
        for i in faculty_data:
            if max_marks[0] == i["Subject"]:
                msg = f'The faculty with highest pass percentage {i.get("Faculty")} and his subject is {i.get("Subject")}'
                print(i)
    return msg
print(highest_pass_percentage('Assignments1/student_marks.csv', 'Assignments1/subject_faculty.csv'))



