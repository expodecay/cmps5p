__author__ = 'Rick'
#Rick Ramirez
#riryrami@ucsc.edu
#programming assignment 5
#This program uses lists and dictionaries to print the first ten verses of "the ants go marching".


	#Define two lists, one to count the verses and one to describe the little ants actions.
	#verse will serve as the keys for a dictionary since a dictionary does not itself follow indices.
verse = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
action = ['suck his thumb', 'tie his shoe', 'climb a tree', 'shut the door', 'take a dive', 'pick up sticks',
        'look up to heaven', 'shut the gate', 'check the time', 'say the end']
	#The rest of the song is stored in a single string.
ending = "And they all go marching down...\nIn the ground...\nTo get out...\nOf the rain.\nBoom! Boom! Boom!"

#This function generates a dictionary from the lists verse and action.
#verse becomes the keys, and action becomes the values of the corresponding key.
def dictionary(ky, val):
    dicts = {}
    for i in range(len(ky)):
        dicts[ky[i]] = val[i]
    return dicts

#The main function loops through the dictionary and uses for loops to print the song.
def main():
	#call the dictionary_generator
    x = dictionary(verse, action)
	#The list verse verves to set the length of the iteration, and as a method of ordering the iterations.
    for j in range(len(verse)):
        for i in range(3):
            print("The ants go marching", verse[j], "by", verse[j]+",", end="")
            if i != 2:
                print(" hurrah! Hurrah!")
            else:
                print("")
		#The value of each dictionary key (for the current verse) is printed.
        print("The little one stops to", x[verse[j]]+',')
		#The rest of the song is printed.
        print(ending)
main()
