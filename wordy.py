__author__ = 'Rick'
#Rick Ramirez
#riryrami@ucsc.edu
#programming assignment 3
#This program counts the number of words and the average word length of a string provided by the users input.

def main():
	#User input can consist of any character.
	message = input("Please write a sentence. ")
	#The input becomes a parameter for the remove-punctuation function.
	remove_punct(message)


#The punctuation marks that are not to be considered are removed.
def remove_punct(message):
		#The input is converted into a list, with each element determined by the spaces of the input string.
	list = message.split()
		#Punctuation to be removed is stored in a list.
	punct = [".", ",", "!", "?"]
		#An empty list is initialized and will be populated with the stripped elements of the original list.
	empty = []
		#Consider each element of the original list.
	for word in list:
		for symbol in punct:
				#If a symbol from the punct list is found in the current element, it is replaced with an empty string.
			word = word.replace(symbol,"")
		empty.append(word)
		#If an element of the new list consists only of an empty string, it is removed.
	curtailed = [x for x in empty if x != ""]
	print("Your sentence has", len(curtailed), "words.")
		#The curtailed list becomes the parameter for the function word_length.
	word_length(curtailed)


#The size of each element of the new list is evaluated and accumulated.
def word_length(curtailed):
	count = 0
	for word in curtailed:
			#Length of each element is accumulated.
		count += len(word)
	if count == 0:        #This statement prevents the program from crashing in the event that the user enters an empty string, or a string containing only the symbols (.,!?)
		print("The average word length of your sentence is approximately " +str(count)+".")
	#The total number of sub-elements calculated is compared to the size of the list and is printed with two decimal places.
	else:
		print("The average word length of your sentence is approximately  " + str(round(count / len(curtailed), 2))+".")

main()