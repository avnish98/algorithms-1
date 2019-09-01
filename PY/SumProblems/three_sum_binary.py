""" Implementing 3 sum problem with binary search
    Takes n^2 log n time to converge"""
    
import sys
import timeit
from math import log2

def binary_search(arr, low, high, j):
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
            return 1
    
    else : 
        return -1
    
class three_sum_binary:
    def __init__(self, file):
        self.time = 0
        self.exptime = 0
        with open(file, "r") as array:
            self.arr = list(map(lambda x: int(x), array))
            self.length = len(self.arr)
    
    def binary(self):
        start = timeit.default_timer()
        found = 0
        count = 0
        for i in range(self.length):
            for j in range(i+1, self.length):
                found = binary_search(self.arr, 0, len(self.arr), 
                             (-(int(self.arr[i]+self.arr[j]))))
                if(found == -1):
                    break
                else:
                    count += 1
        stop = timeit.default_timer()
        self.time = stop - start
    
    def timed(self):
        print("Runtime of Brute force algorithm : {}".format(self.time))
        print("Expected runtime of Brute force algorithm : {}".format((self.length**2)*log2(self.length)))

threesum = three_sum_binary(sys.argv[1])
threesum.binary()
threesum.timed()
