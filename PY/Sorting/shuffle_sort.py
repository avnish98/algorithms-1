""" Implementing Shuffling
    Generating a random number for each element and sorting array using that number """

import random
from collections import OrderedDict

def exchange(a, b):
    """ Exchanges the values in variables and returns them """
    temp = a
    a = b
    b = temp
    return a, b

def compare(a, b):
    """ Compares first element with second """
    if(a < b):
        return -1

    elif(a > b):
        return 1

    else:
        return 0

def less(v, w):
    """ Returns True if first element is smaller than second """
    return bool(compare(v, w) < 0)

def is_sorted(a):
    """ Returns True if sorted """
    for i in range(len(a)):
        if (less(a[i], a[i-1])):
            return False
    return True

def selection_sort(a):
    """ Performs selection sort on array """
    for i in range(len(a)):
        min = i                               # Select element and assume it to be min
        for j in range(i+1, len(a)):          # For every element next to it
            if (less(a[j], a[min])):          # Check if less 
                min = j                       # Set it as min
        a[i], a[min] = exchange(a[i], a[min]) # Exchange it with min value
    
    return a

def shuffle(a):
    """ Shuffles a list and prints it on console """
    # Creating a list of random numbers
     r_list = []
    for r in range(len(a)):
        num = random.randint(0, (len(a)-1))
        r_list.append(num)

    # Mapping random numbers to original list
    mapping = OrderedDict(zip(r_list, a))
    
    # Sorting random numbers using selection sort
    r_list_sorted = selection_sort(r_list)

    # Using mapping to generate new shuffled list
    shuffled_list = []
    for r in r_list_sorted:
        shuffled_list.append(mapping[r])

    print(shuffled_list)

shuffle([9, 7, 2, 34, 532,2,3, 2, 543, 2, 2, 3, 34, 4,3 ,2, 3,32 ,34, 34,324 ,324 ])
        


