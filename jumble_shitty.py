__author__ = 'Rick'
__author__ = 'Rick'

# Call the main function with a parameter set to a file location in the form of a string.
# file location:     "/users/rick/desktop/words.txt"
# words to check:     lsitNe   prinsg   cokie

import math

def get_word():
    x = input("Please enter a jumbled word: ")
    return x

def word_mod(word):
    return word.lower()

# ALL PERMUTATIONS OF THE USER'S WORD.
def anagram(jum):
    if jum == "":
        return [jum]
    else:
        ans = []
        for w in anagram(jum[1:]):
            for pos in range(len(w)+1):
                ans.append(w[:pos] + jum[0] + w[pos:])
    return ans

# BRING IN A DICTIONARY AND MAKE A LIST OF ALL IT'S WORDS IN LOWERCASE.
def get_dict(file):
    dictTxt = open(file, "r")
    contents = dictTxt.read()
    contents = contents.replace("\n", " ")
    list_of_words = contents.lower().split()
    return list_of_words



def main(file_location):
    dictionary = get_dict(file_location)
    x = get_word()
    y = word_mod(x)
    anagram(y)
    for i in anagram(y):
        if i in dictionary:
            print(i)


