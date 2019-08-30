""" Implementing Binary Search
    Takes log N time to converge """

from math import log2
from timeit import default_timer

start = default_timer()

def search(arr, high, low,  j):
    arr_len = len(arr)
    mid = int(low + (high-low)/2)

    if(low >= high):

        # Search left if less than mid
        if(j < arr[mid]):
            search(arr, low, mid-1, j)
        
        # Seach right if greater than mid
        elif(j > arr[mid]):
            search(arr, mid+1, high, j)
        
        # Element found at mid
        elif(j == arr[mid]):
            print("Element {} found".format(j))
    
    else : 
        print("Element not found")
   
t = [1, 2, 3, 4, 5, 11, 40, 200, 321, 344, 2333]
search(t, 0, len(t), 401)
        
stop = default_timer()
print("Runtime of binary search : {}".format(stop-start))
print("Expected runtime of binary search : {}".format(log2(len(t))))