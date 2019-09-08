""" Implementing Dijkstra's 2-stack algorithm for solving expressions

    There are two stack : Operator stack and Operand Stack
    For each item in expression :
        if item = "("      then ignore
        if item = digit    then push to operand stack
        if item = operator then push to operator stack
        if item = ")"      then pop two operands from operand stack
                                pop operator from operator stack
                                perform operation
                                push result back onto operand stack 
    
    Final answer will be on operand stack                           """

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


exp = input("Enter the expression:")
op = Stack() #Operand Stack
opr = Stack() #Operator Stack
op_list = ["+", "-", "*", "/"] #List of operations

for ex in exp:
    if (ex == "("):
        pass
    elif (ex.isdigit()):
        op.push(ex)
    elif (ex in op_list):
        opr.push(ex)
    elif (ex == ")"):
        op1 = op.pop()
        op2 = op.pop()
        opr = opr.pop()
        op3 = eval(str(op1)+opr+str(op2))
        op.push(op3)

print(op.pop())
