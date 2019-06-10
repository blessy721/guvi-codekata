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
        if middle_node is None:
            print("location unavailable")
            return
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
    def search(self,dat):
        current=self.head
        if current is None:
            print("Empty linked list")
            return
        while current is not None:
            if current.data==dat:
                return True
            current=current.nextval
        return False
    #def mainmenu(self):









obj=LinkedList()
obj.head=Node("Hey")
a=Node("How")
b=Node("are you")
obj.head.nextval=a
a.nextval=b
n=int(input("Welcome!\nPlease select from the following options\n1.Insert at the beginning of linked list\n2.Insert at the middle of linked list\n3.Insert at the end of linked list\n4.Delete a node in linked list\n5.Search for data\n6.Exit\n7.Show all the nodes inside the linked list\n"))
#print(type(n))#obj.mainmenu()
#for i in range(7):
    #n=input("Welcome!\nPlease select from the following options\n1.Insert at the beginning of linked list\n2.Insert at the middle of linked list\n3.Insert at the end of linked list\n4.Delete a node in linked list\n5.Search for data\n6.Exit\n")
if (n==1):
    dat=str(input("Enter your data : "))
    obj.insertbeg(dat)
    print("Operation successful!")
elif n==3:
    dat=input("Enter your data : ")
    obj.insertend(dat)
    print("Operation successful!")
elif n==2 :
    dat=input("Enter your data : ")
    obj.inbetween(obj.head.nextval,dat)
    print("Operation successful!")
elif n==4:
    dat=input("Enter data to delete")
    obj.removenode(dat)
    print("Operation successful!")
elif n==5:
    dat=input("Enter text to find : ")
    if obj.search(dat):
        print("Yes")
    else:
        print("No")
elif n==6:
    print("Thank You! Please don't come again. GOODBYE!!")
elif n==7:
    obj.printll()
else:
    print("Please enter a valid option")


    #n=input("Welcome!\nPlease select from the following options\n1.Insert at the beginning of linked list\n2.Insert at the middle of linked list\n3.Insert at the end of linked list\n4.Delete a node in linked list\n5.Search for data\n6.Exit\n")
