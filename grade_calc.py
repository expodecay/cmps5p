__author__ = 'Rick'
# Rick Ramirez
# riryrami@ucsc.edu
# programming assignment 7
# This program takes all quiz and programming scores from the user and calculates an average for each. Then the program calculates
# the current grade in the class. The user is then asked for a desired total grade, and the program calculates minimum final grade to
# produce the desired total.

# get the quiz scores in the form of a list.
def get_list():
    quiz_grades = eval(input("Please enter your quiz scores as a list: "))
    return quiz_grades

# drop the lowest quiz grade by sorting the quizzes and removing the first element in the list.
def drop_lowest():
    grades = get_list()
    for score in range(len(grades)):
        if grades[score] < 0 or grades[score] > 20:
            grades = eval(input("That was not a valid list of scores. Please enter your quiz scores (between 0 "
                                "and 20) as a list: "))
        else:
            pass
    return grades

# calculate the average quiz grade.
def quiz_avg(grades):
    total = 0
    print("You entered " + str(len(grades)) + " scores (by the end of the quarter there should be 5), ", end="")
    grades.sort()
    if len(grades) > 1:
        grades.remove(grades[0])
    else:
        pass
    for score in grades:
        total = total + score
    print("your current quiz average (with the lowest score dropped) is " + str(round(100*total/(len(grades)*20)))
          + "%.")
    avg_quiz_score = 100*total/(len(grades)*20)
    return avg_quiz_score

# ask the user for the grades received on each assignment.
def get_programs():
    prgm_grades = []
    max = [10, 20, 20, 30, 20, 30]
    for asgmt in range(6):
        while True:
            grade = eval(input("Please enter your score for programming assignment "
                               + str(asgmt+1)+" (out of " + str(max[asgmt])+" points): "))
            if grade < 0 or grade > max[asgmt]:
                print("That score was not in range 0 to " + str(max[asgmt]) + ".", end=" ")
            if max[asgmt] >= grade >= 0:
                prgm_grades.append(grade)
                break
    extra = eval(input("Please enter your score for the extra credit assignment (out of 10 points): "))
    prgm_grades.append(extra)
    return prgm_grades

# calculate an average of the programming grades. If the extra credit pushes the average over 100%, the average is set to exactly 100%.
def programming_avg(prgm_scores):
    total = 0
    max_points = 0
    max = [10, 20, 20, 30, 20, 30, 10]
    for i in range(len(prgm_scores)-1):
        max_points += max[i]
    for score in prgm_scores:
        total = total + score
    avg_prgm_score = (total/max_points)*100
    if avg_prgm_score > 100:
        avg_prgm_score = 100
    print("Your programming assignment average is " + str(round(avg_prgm_score)) + "%.")
    return avg_prgm_score

# the current total grade is calculated by considering the weight of both quizzes and assignments.
def weighted_grade(avg_quiz, avg_prgm):
    quiz_weight = avg_quiz * 30
    program_weight = avg_prgm * 45
    total_grade = (quiz_weight + program_weight)/75
    print("Right now you have a " + str(round(total_grade)) + "% in the class.")
    return total_grade

# ask the user for a desired grade for the course.
def desired_grade():
    options = {"A": 90, "B": 80, "C": 70}
    want = (input("What grade do you wish to receive in the class (A, B, or C)? "))
    while True:
        if want != "A" and want != "B" and want != "C":
            print("You did not enter a valid grade. ", end="")
            want = (input("What grade do you wish to receive in the class (A, B, or C)? "))
        else:
            break
    return options[want]

# determine the grade the user needs on the final to produce the desired course grade.
def what_you_need(what_you_want, avg_quiz, avg_prgm):
    final_weight = 0.25
    prgm_quiz_weight = avg_quiz * 0.3 + avg_prgm * .45
    print("You need to get at least a " + str(round((what_you_want - prgm_quiz_weight)/final_weight)) +
          "% on the final exam to get your desired grade.")

def main():
    get_quiz_grades = drop_lowest()
    get_program_grades = get_programs()
    average_quiz_score = quiz_avg(get_quiz_grades)
    average_programming_score = programming_avg(get_program_grades)
    weighted_grade(average_quiz_score, average_programming_score)
    wanted_grade = desired_grade()
    what_you_need(wanted_grade, average_quiz_score, average_programming_score)

main()


