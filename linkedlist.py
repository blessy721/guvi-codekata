class Node:
    def __init__(self,data=None):
        self.data=data
        self.nextval=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printll(self):
        printval=self.head
        while printval is not None:
            print(printval.data)
            printval=printval.nextval
    def insertbeg(self,newval):
        newnode=Node(newval)
        newnode.nextval=self.head
        self.head=newnode
    def insertend(self,new):
        newnode=Node(new)
        if self.head==None:
            self.head=newnode
            return
        last=self.head
        while(last.nextval):
            last=last.nextval
        last.nextval=newnode
    def inbetween(self,middle_node,new):
        if middle_node is not None:
            print("location unavailable")
        newnode=Node(new)
        newnode.nextval=middle_node.nextval
        middle_node.nextval=newnode
    def removenode(self,dat):
        headval=self.head
        if headval is not None:
            if (headval.data==dat):
                self.head=headval.nextval
                headval=None
                return
        while headval is not None:
            if headval.data==dat:
                break
            prev= headval
            headval=headval.nextval
        if headval==None:
            return
        prev.nextval=headval.nextval
        headval=None



obj=LinkedList()
obj.head=Node("Hey")
a=Node("How")
b=Node("are you")
obj.head.nextval=a
a.nextval=b
obj.insertbeg("Nigga")
obj.insertend("niggatron")
obj.inbetween(a,"YOYOYOYO")
obj.removenode("niggatron")
obj.printll()
