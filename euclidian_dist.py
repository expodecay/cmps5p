__author__ = 'Rick'
# calculates the Euclidean Distance between  two points.

import math

def euclid():
    xa, ya, za = eval(input("coordinates of first point: "))
    xb, yb, zb = eval(input("coordinates of second point: "))
    dist = math.sqrt((xa - xb)**2 +(ya - yb)**2 + (za - zb)**2)
    print(dist)
    return dist

euclid()