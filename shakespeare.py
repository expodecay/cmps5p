__author__ = 'Rick'
#Rick Ramirez
#riryrami@ucsc.edu
#programming assignment 4
#This program takes a file as a parameter, and returns a dictionary where the keys are the words and the values are the number of times the word appears.
import string

#The variable file is entered (by the user) as the location of the file to be processed.
def main(file):
	#Open the file in reading mode, read in the file, and remove the new line characters.
	book = open(file, "r")
	contents = book.read()
	contents = contents.replace("\n", " ")

	#Loop through the file (which is now in for form of a continuous string) and remove all punctuation.
	symbols = string.punctuation
	for ch in symbols:
		contents = contents.replace(ch, "")

	#remove all capitalization in the string, and create a list from the curtailed string.
	list_of_words = contents.lower().split()

	#Initialize a dictionary.
	dict = {}
	#loop through the list of words.
	#Each new word becomes a key, and  is given a value of 1. If the word appears again, its occurrence us updated.
	for word in list_of_words:
		if word in dict:
			dict[word] = dict[word] + 1
		else:
			dict[word] = 1

	return (dict)

