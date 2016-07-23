__author__ = 'Rick'
#Rick Ramirez
#riryrami@ucsc.edu
#programming assignment 0
#This program takes a distance in kilometers from the user, converts the value to miles, then prints the result.

def convert():
	kilo = eval(input("What is the distance in kilometers?:  "))
	mile = kilo * 0.62
	print("The distance in miles is", mile)

convert()