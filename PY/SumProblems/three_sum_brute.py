import sys
import timeit

class three_sum_brute:
    def __init__(self, file):
        self.time = 0
        self.exptime = 0
        with open(file, "r") as array:
            self.arr = list(array)
            self.length = len(self.arr)
    
    def brute(self):
        count = 0
        start = timeit.default_timer()
        for i in range(self.length):
            for j in range(i+1, self.length):
                for k in range(j+1, self.length):
                    if ((self.arr[i]+ self.arr[j] + self.arr[k]) == 0):
                        count += 1
        stop = timeit.default_timer()
        self.time = stop - start
        print(count)
    
    def timed(self):
        print("Runtime of Brute force algorithm : {}".format(self.time))
        print("Expected runtime of Brute force algorithm : {}".format(self.length**3))

threesum = three_sum_brute(str(sys.argv[1]))
threesum.brute()
threesum.timed()



