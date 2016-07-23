__author__ = 'Rick'
#Rick Ramirez
#riryrami@ucsc.edu
#programming assignment 2
#This program calculates the average of the scores provided by the user.

#The user is asked for the number of grades to be entered.
def main():
	#If the user enters a float or a negative number, the loop repeats itself.
	#Once an integer is  entered, the loop is broken.
	while True:
		class_size = eval(input("How many grades will you be entering? "))
		if class_size <= 0.0:
			print("You can't enter", class_size, "grades! ", end="")
		if type(class_size) != int:
			print("You can't enter", class_size, "grades! ", end="")
		if type(class_size) == int and class_size > 0:
			break
	#The integer that the user enters is stored under the variable num.
	#num becomes the parameter for the function grade_accum(class_size).
	num = class_size
	grade_accum(num)

#The total number of grades accumulates.
def grade_accum(class_size):
	#The range of allowed scores are given variable names, and the total is initialized.
	min_grade = 0
	max_grade = 100
	total = 0
	#The length of the for loop is determined by the users input from the main function.
	for student in range(class_size):
		#This while loop is repeated until the user enters a number within the range of acceptable scores.
		while True:
			score = eval(input("Please enter a grade between 0 and 100: "))
			if score < min_grade or score > max_grade:
				print("Your number is out of range! ", end="")
			#When a score falls within the appropriate range, the while loop is broken, and the next (student) index iterates.
			if score >= min_grade and score <= max_grade:
				#The total is accumulated, and becomes a parameter for the function average(total, class_size).
				total = total + score
				break
	average(total, class_size)

#The total accumulated scores is compared to the size of the class, and an class performance is determined.
def average(total, class_size):
	avg_score = total / class_size
	if avg_score < 70:
		print("Your class did poorly. The average was",avg_score)
	if avg_score >= 70:
		print("Your class did great! The average was",avg_score)


main()

