""" Implementing stack using List
    Works on Last In First Out (LIFO) principle """

class Stack:
    def __init__(self):
        self.arr = []
    
    def display(self):
        print(self.arr)

    def pop(self):
        last = self.arr.pop(0)
        return(last)

    def push(self, item):
        self.arr = [item] + self.arr

    def is_empty():
        if (len(self.arr) == 0):
            return True
        return False
    
    def size(self):
        return len(self.arr)

stack = Stack()
stack.push(2)
stack.push(3)
stack.push(9)
print(stack.size())
stack.display()
stack.pop()
stack.display()
