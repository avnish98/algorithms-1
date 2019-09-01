""" Implementing Linked List
    It consists of nodes (a value and address of next item) """

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        i = self.head
        while(i != None):
            print("{} ->".format(i.item), end=' ')
            i = i.next
        print('\n')

llist = LinkedList()

llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third

llist.display()