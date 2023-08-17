import csv

faculty = {
    'Telugu': 'Amarnath',
    'English': 'Samuel',
    'Maths': 'Murali Krishna',
    'Physics': 'Raja Gopal',
    'Chemistry': 'Ravi',
    'Social': 'Krishna Reddy'
}

pass_mark = 40

def get_student_marks(file_path):
    with open(file_path, 'r') as file:
        data = csv.DictReader(file)
        student_marks = []
        for record in data:
            marks = [
                int(record['Telugu']),
                int(record['English']),
                int(record['Maths']),
                int(record['Physics']),
                int(record['Chemistry']),
                int(record['Social'])
            ]
            student_marks.append((record['studentname'], marks))
        return student_marks

def get_subject_counts(marks_list, threshold):
    counts = [0] * len(faculty)
    for student, marks in marks_list:
        for i, mark in enumerate(marks):
            if mark >= threshold:
                counts[i] += 1
    return counts

def get_highest_count_faculty(counts):
    max_count = max(counts)
    max_index = counts.index(max_count)
    subject = list(faculty.keys())[max_index]
    return faculty[subject], max_count

def get_lowest_count_faculty(counts):
    min_count = min(counts)
    min_index = counts.index(min_count)
    subject = list(faculty.keys())[min_index]
    return faculty[subject], min_count

def get_top_student_with_max_total(student_marks):
    total_scores = [(student, sum(marks)) for student, marks in student_marks]
    top_student = max(total_scores, key=lambda x: x[1])
    return top_student

def get_best_student_in_subject(student_marks, subject_index):
    best_student = ''
    highest_marks = 0
    for student, marks in student_marks:
        if marks[subject_index] >= 90 and marks[subject_index] > highest_marks:
            highest_marks = marks[subject_index]
            best_student = student
    return best_student, highest_marks

def get_average_marks(marks_list):
    subject_sums = [0] * len(faculty)
    subject_counts = [0] * len(faculty)
    
    for _, marks in marks_list:
        for i, mark in enumerate(marks):
            if mark >= pass_mark:
                subject_sums[i] += mark
                subject_counts[i] += 1
    
    avg_marks = [round(total / count) if count > 0 else 0 for total, count in zip(subject_sums, subject_counts)]
    return avg_marks

def get_student_with_least_total(student_marks):
    total_scores = [(student, sum(marks)) for student, marks in student_marks]
    least_student = min(total_scores, key=lambda x: x[1])
    return least_student

file_path = 'C:/Users/teju2/Desktop/workstation/testprograms/Assignments1/student_marks.csv'
student_marks = get_student_marks(file_path)

# Find the faculty with the highest student count who scored more than 90%
subject_counts = get_subject_counts(student_marks, 90)
faculty_highest_score = get_highest_count_faculty(subject_counts)
print(f"The faculty with the highest number of students scoring more than 90% is {faculty_highest_score[0]} with {faculty_highest_score[1]} students.")

# Find the faculty with the highest pass percentage (>40)
subject_counts = get_subject_counts(student_marks, pass_mark)
faculty_highest_pass_percentage = get_highest_count_faculty(subject_counts)
pass_percentage = (faculty_highest_pass_percentage[1] / len(student_marks)) * 100
print(f"The faculty with the highest pass percentage (>40) is {faculty_highest_pass_percentage[0]} with {pass_percentage:.2f}% students.")

# Find the faculty with the least pass percentage (<=40)
faculty_lowest_pass_percentage = get_lowest_count_faculty(subject_counts)
low_pass_percentage = (faculty_lowest_pass_percentage[1] / len(student_marks)) * 100
print(f"The faculty with the least pass percentage (<=40) is {faculty_lowest_pass_percentage[0]} with {low_pass_percentage:.2f}% students.")

# Find the top student with maximum total
top_student = get_top_student_with_max_total(student_marks)
print(f"The top student is {top_student[0]} with a total score of {top_student[1]}.")

# Find the best student in mathematics
best_math_student = get_best_student_in_subject(student_marks, 2)
print(f"The best student in Mathematics is {best_math_student[0]} with a score of {best_math_student[1]}.")

# Find the average marks for each subject (ignoring failures)
avg_marks = get_average_marks(student_marks)
for i, subject in enumerate(faculty):
    print(f"Ignoring failures, the average mark for {subject} is {avg_marks[i]}.")

# Find the student with the least total marks
least_student_total = get_student_with_least_total(student_marks)
print(f"The student with the least total marks is {least_student_total[0]} with a total of {least_student_total[1]}.")
