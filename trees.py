class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left==None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right==None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data

    def findval(self,dat):
        if dat<self.data:
            if self.left is None:
                return str(self.left)+" Not found"
            return self.right.findval(dat)
        elif dat>self.data:
            if self.right is None:
                return str(self.right)+" Not found"
            return self.right.findval(dat)
        else:
            return str(self.data)+" found"




    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.data),
        if self.right:
            self.right.printtree()


obj=Node(21)
obj.insert(12)
obj.insert(23)
obj.insert(221)
obj.insert(234)
obj.insert(236)

obj.printtree()
print(obj.findval(234))
print(obj.findval(235))
print(obj.findval(12))
print(obj.findval(13))
