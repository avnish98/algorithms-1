""" Implementing stack using Linked List
    Works on Last In First Out (LIFO) principle 
    Added a program that takes string input:
    pop         => if input is "-"
    display     => if input is "d"
    push        => for every other input """

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:
    def __init__(self, head):
        self.head = head
    
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
        newitem = Node(item)
        oldhead = self.head

        self.head = newitem
        newitem.next = oldhead

    def is_empty():
        if (self.head == None):
            return 1
        return 0
    
    def size(self):
        count = 0
        i = self.head
        while(i != None):
            count += 1
            i = i.next
        return count

stack = Stack(Node(1))
while(1):
    inp = input("Enter your item :")
    if(inp == "-"):
        stack.pop()
    elif(inp == 'd'):
        stack.display()
    else:
        stack.push(int(inp))
