class Node:
    def __init__(self):
        self.stack=[]
    def push(self,st):
        for i in st:
            self.stack.append(i)
    def popp(self,st):
        for i in range(len(st)):
            if st[i] in self.stack:
                self.stack.pop()
    def printstack(self):
        if len(self.stack)>0:
            print("NO")
        else:
            print("YES")
obj=Node()
st=str(input())
obj.push(st)
obj.popp(st)
obj.printstack()
