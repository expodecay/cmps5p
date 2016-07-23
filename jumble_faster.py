__author__ = 'Rick'
# Rick Ramirez
# riryrami@ucsc.edu
# Assignment 6
# This program takes as a parameter, a file text location in the form of a string. The words in the file are stored in a dictionary.
# The user is asked for a random string of letters. Using a permutation generator and dictionary methods, the anagrams of the users
# input are determined (by comparing the permutations to the keys of the dictionary) and printed. If no permutations are found in the
# dictionary keys, the program prints that there are no anagrams.

def get_dictionary(file):
    book = open(file, "r")
    contents = book.read()
    contents = contents.replace("\n", " ")
    list_of_words = contents.lower().split()
    dict = {}
    #   loop through the list of words.
    #   Each new word becomes a key, and  is given a value of 1.
    for word in list_of_words:
            dict[word] = 1
    return dict

def get_word():
    word = input("Please enter a jumbled word: ")
    return word.lower()

def permut_list(word):
    #base case
    if word == "":
        return([word])
    else:
        #recurse on the length of the word. place the first letter in all positions in each word of anagram(remaining letters of the word).
        short_word = word[1:]
        first_letter = word[0]
        fresh_list = []
        for small_mixed_word in permut_list(short_word):
            for i in range(len(small_mixed_word) + 1):
                fresh_list.append(small_mixed_word[0:i] + first_letter + small_mixed_word[i:])
        # remove multiple occurrences. Example: "anagram"
        clean = []
        for i in fresh_list:
            if i not in clean:
                clean.append(i)
        return clean

def main(filename):
    jumbled = get_word()
    dictionary = get_dictionary(filename)
    permutations = permut_list(jumbled)

    # remove the jumbled word to ensure that the length of the list (i.e. the corresponding if statement)
	# is valid when anagram candidates are evaluated.
    # Example: 'ana' will print: "your wordS ARE naa" instead of "WORD IS naa"

    permutations.remove(jumbled)

    # if the permutation is a word in the dictionary, add to list.
    anagrams = []
    for i in permutations:
        if i in dictionary:
            anagrams.append(i)
        else:
            pass
    if len(anagrams) == 1:
        print("Your word is "+str(anagrams[0])+".")

    elif len(anagrams) > 1:
        print("Your words are:")
        for i in anagrams:
            print(i)
    else:
        print("Your word cannot be unjumbled.")

# Don't return the list of anagrams!!
# if you return them, they will get printed when the main function is called, and
# if the user sets a variable to the main function, then that variable will just
# contain the list of anagrams instead of asking for a new word.



