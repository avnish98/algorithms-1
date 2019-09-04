""" Implementing stack using Linked List
    Works on Last In First Out (LIFO) principle """

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def display(self):
        i = self.head
        while(i != None):
            print("  {}".format(i.item))
            print("-----")
            i = i.next
    
    def pop(self):
        i = self.head

        if(i == None):
            print("Stack Underflow")
            return -1

        self.head = self.head.next
        return(i.item)

    def push(self, item):

        if(self.head == None):
            self.head = Node(item)
        
        else:
            newitem = Node(item)
            oldhead = self.head

            self.head = newitem
            newitem.next = oldhead

    def is_empty():
        if (self.head == None):
            return True
        return False
    
    def size(self):
        count = 0
        i = self.head
        while(i != None):
            count += 1
            i = i.next
        return count

stack = Stack()
stack.push(2)
stack.push(3)
stack.push(9)
print(stack.size())
stack.display()
stack.pop()
print()
print()
stack.display()
