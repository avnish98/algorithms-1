""" Implementing Queue using List
    It works on First In First Out (FIFO) Principle """

class Queue:
    def __init__(self):
        self.arr = []
    
    def enqueue(self, item):
         self.arr.append(item)
    
    def dequeue(self):
        if (self.size() == 0):
            print("Empty Queue")
            return -1
        i = self.arr[0]
        self.arr.pop(0)
        return i
    
    def is_empty(self):
        if(len(self.arr) == 0):
            return True
        return False

    def size(self):
        return len(self.arr)

    def display(self):
        print(self.arr)

queue = Queue()
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(9)
print(queue.size())
queue.display()
queue.dequeue()
queue.dequeue()
queue.display()