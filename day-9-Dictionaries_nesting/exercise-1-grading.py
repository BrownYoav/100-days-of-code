student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
	score = student_scores[student]
	
	if 90 < score < 101:
		grade = 'Outstanding'
	elif 80 < score < 91:
		grade = 'Exceeds Expectations'
	elif 70 < score < 81:
		grade ='Acceptable'
	else:
		grade = 'Fail'

	student_grades[student] = grade

# 🚨 Don't change the code below 👇
print(student_grades)