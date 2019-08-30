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
            print("Element {} found".format(j))
    
    else : 
        print("Element not found")
    
class three_sum_binary:
    def __init__(self, file):
        self.time = 0
        self.exptime = 0
        with open(file, "r") as array:
            self.arr = list(map(lambda x: int(x), array))
            self.length = len(self.arr)
    
    def binary(self):
        start = timeit.default_timer()
        for i in range(self.length):
            for j in range(i+1, self.length):
                binary_search(self.arr, 0, len(self.arr), 
                             (-(int(self.arr[i]+self.arr[j]))))
        stop = timeit.default_timer()
        self.time = stop - start
    
    def timed(self):
        print("Runtime of Brute force algorithm : {}".format(self.time))
        print("Expected runtime of Brute force algorithm : {}".format((self.length**2)*log2(self.length)))

threesum = three_sum_binary(sys.argv[1])
threesum.binary()
threesum.timed()
