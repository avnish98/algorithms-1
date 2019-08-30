import sys
import timeit

start = timeit.default_timer()

class three_sum_brute:
    def __init__(self, file):
        with open(file, "r") as array:
            self.arr = list(array)
            self.length = len(self.arr)
    
    def brute(self):
        count = 0
        
        for i in range(self.length):
            for j in range(i+1, self.length):
                for k in range(j+1, self.length):
                    if ((self.arr[i]+ self.arr[j] + self.arr[k]) == 0):
                        count += 1

        print(count)

threesum = three_sum_brute(str(sys.argv[1]))
threesum.brute()
stop = timeit.default_timer()

print("Runtime of Brute force algorithm : {}".format(start - stop))
