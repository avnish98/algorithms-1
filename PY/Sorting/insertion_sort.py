""" Implementing Insertion Sort
    In each iteration swap with each smaller element to its left
    Takes n^2 time to converge                          """

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

def insertion_sort(a):
    """ Performs insertion sort on array """
    for i in range(len(a)):                      
        for j in range(i+1, len(a)):              # For every element next to current element
            if (less(a[j], a[i])):                # If less than current element
                a[i], a[j] = exchange(a[i], a[j]) # Exchange it
    print(a)
    
insertion_sort([9, 7, 2, 34, 532,2,3, 2, 543, 2, 2, 3, 34, 4,3 ,2, 3,32 ,34, 34,324 ,324 ])