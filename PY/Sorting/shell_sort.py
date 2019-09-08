""" Implementing Shell Sort (named after Donald Shell)
    First h-sort array then decrease the value of h 
    and h-sort again till completely sorted
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

def shell_sort(a):
    """ Performs shell sort on array """

    # Using Donald Knuth's (3^x-1)/2 increment sequence
    inc_seq = [int(((3**x)-1)/2) for x in range(1, int(len(a)/3))]
    
    for inc in sorted(inc_seq, reverse=True):
        for i in range(len(a)):
            try:
                # Same as performing insertion sort but with increment
                for j in range(i+inc, len(a)):
                    if (less(a[j], a[i])):                 # If less than current element
                         a[i], a[j] = exchange(a[i], a[j]) # Exchange it
            except IndexError:                             # Change increment gap
                break
        print("{} sorted : {}".format(inc,a))

    print("Final Sorted array: {}".format(a))


shell_sort([9, 7, 2, 34, 532,2,3, 2, 543, 2, 2, 3, 34, 4,3 ,2, 3,32 ,34, 34,324 ,324 ])