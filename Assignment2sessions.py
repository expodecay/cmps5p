__author__ = 'Rick'
import math

def main():

    num = eval(input("How many grades will you be entering? "))
    count = 0
    while count < num:
     if type(num) == float:
        print("You can't enter", num, "grades!", end="")
        num = eval(input("How many grades will you be entering? "))
    if type(num) == int:
        print(num)
    for num in range(num):
        grade = eval(input("Please enter a grade between 0 and 100: "))
        if grade < 0 or grade > 100:
            print("Your number is out of range! ", end="")
            grade = eval(input("Please enter a grade between 0 and 100: "))
        average = grade + 1000
        print(average)
main()