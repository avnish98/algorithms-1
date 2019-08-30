import sys
import timeit

start = timeit.default_timer()

class two_sum:
    def __init__(self, file):
        with open(file, "r") as array:
            self.arr = list(array)
            self.length = list(self.arr)

    def brute(self):
        count = 0
        for i in range(0, self.length):
            for j in range(i+1, self.length):
                if (self.arr[i] + self.arr[j] == 0):
                    count += 1
        print(count)

twosum = two_sum(str(sys.argv[0]))
twosum.brute()

stop = timeit.default_timer()
print("Runtime of brute force algorithm : {}".format(start - stop))