__author__ = 'Rick'
#Rick Ramirez
#riryrami@ucsc.edu
#programming assignment 1
#This program produces a random integer between 1 and 10, then asks the user to guess what it is. The user is given three attempts.

#The random module generates pseudo-random numbers.
#We use the randint() function within the random module to generate a random integer.
import random

def main():
	#A random integer is generated and the number of turns is initialized.
	num = random.randint(1, 10)
	print("I'm thinking of an integer, you have three guesses.")
	turns = 3

	for turn in range(turns):
	#The number of turns remaining is updated, and the user is asked to guess the integer.
	#The users input is added to the end of the print statement.
		print("Guess", turn+1, ":  ", end = "")
		guess = eval(input("Please enter an integer between 1 and 10:  "))
		#if the user guesses correctly, or the max number of attempts is reached, the loop ends.
		#if neither are fulfilled, the else statement takes over, and the loop repeats.
		if guess == num:
			print("You got it!")
			break
		#The for loop starts at zero, so the max number of turns is 2.
		if turn == 2:
			print("Too bad. The number is:", num)
			break
		else:
			if guess < num:
				print("Your guess is too small.")
			elif guess > num:
				print("Your guess is too big.")
main()
