class Node:
    def __init__(self):
        self.stack=[]
    def push(self,dat):
        self.stack.append(dat)
    def popp(self,dat):
        self.stack.pop(dat)
    def printst(self):
        print(self.stack)
obj=Node()
obj.push(12)
obj.push(11)
obj.push(10)
obj.popp(1)
obj.printst()
