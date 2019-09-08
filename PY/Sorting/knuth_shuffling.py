""" Implementing Knuth Shuffling
    For an iteration i, pick a random number r between i and N
    swap elements at ith and rth position """

import random
from collections import OrderedDict

def exchange(a, b):
    """ Exchanges the values in variables and returns them """
    temp = a
    a = b
    b = temp
    return a, b

def knuth_shuffle(a):

    for i in range(len(a)):
        r = int(random.uniform(i, len(a)))
        a[i], a[r] = exchange(a[i], a[r])

    print(a)

knuth_shuffle([9, 7, 2, 34, 532,2,3, 2, 543, 2, 2, 3, 34, 4,3 ,2, 3,32 ,34, 34,324 ,324 ])
        


