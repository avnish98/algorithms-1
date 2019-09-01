""" Implementing stack using Linked List
    Works on Last In First Out (LIFO) principle 
    Added a program that takes file as input:
    pop         => if "-"
    push        => for every other input """

import sys

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
            return True
        return False
    
    def size(self):
        count = 0
        i = self.head
        while(i != None):
            count += 1
            i = i.next
        return count

stack = Stack(Node(1))
with open(sys.argv[1], 'r') as strfile:
    fr = list(strfile.read().split(" "))
    for element in fr:
        if(element == "-"):
            stack.pop()
        else:
            stack.push(element)

stack.display()
