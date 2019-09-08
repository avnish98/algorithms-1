""" Implementing Queue using Linked List
    It works on First In First Out (FIFO) Principle """

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue:
    def __init__(self, head):
        self.head = head
    
    def enqueue(self, item):
        i = self.head
        while (i.next != None):
            i = i.next
        newitem = Node(item)
        i.next = newitem

    def dequeue(self):
        if self.head == None:
            print("Empty Queue")
            return -1

        oldhead = self.head
        self.head = self.head.next
        return (oldhead.item)
    
    def size(self):
        count = 0 
        i = self.head
        while(i != None):
            i = i.next
            count += 1
        return count
    
    def is_empty(self):
        if(self.size == 0):
            return True
        return False
    
    def display(self):
        i = self.head
        while(i != None):
            print("  {}  ".format(i.item), end="|")
            i = i.next
        print()

queue = Queue(Node(1))
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(9)
print(queue.size())
queue.display()
queue.dequeue()
queue.dequeue()
queue.display()