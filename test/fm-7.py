student_marks = {'PHY': 65, 'CHE': 67, 'BIO': 69, 'MATH': 72, 'ENG': 56, 'ICT': 51}
total_marks = 0
subject_list = [];
total_subjects = 0
for subject, mark in student_marks.items():
    subject_list.append(subject)
    total_marks += mark
    print(f"{subject} = {mark}")

total_subjects = len(subject_list)
total_percent = int(total_marks / total_subjects)
print(f"YOU HAVE GOT TOTAL: {total_marks}, MARK PERCENTAGE: {total_percent}%")



