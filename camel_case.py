#python code goes here
#python version :3
class Camel:
    def __init__(self):
        self.s=''
    def conv(self,st):
        s=self.s
        if len(st)==0:
            return
        s=s+(st[0].upper())
        for i in range(1,len(st)):
            if st[i]==' ':
                s=s+' '+st[i+1].upper()
                i+=1
            elif st[i-1] != ' ':
                s=s+st[i]
        print(s)


obj=Camel()
st=str(input())
obj.conv(st)
