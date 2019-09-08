""" Solving Convex Hull Problem
    Finding smallest perimeter to enclose all the points

    How to solve?
    1. Choose point with smalles y-coordinate.
    2. Sort points with polar angle with respect to p.
    3. Discard then only when they make a counter clockwise turn """

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

def convex_hull(a):
    
    # Making a list of all the y-coordinates and sorting it
    y_cord = []

    for item in a:
        y_cord.append(item[1])

    y_cord_sorted = selection_sort(y_cord)

    relative_cord = []
    for 


