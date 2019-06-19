x,y=map(int,input().split())
arr=list(map(int,input().split()))
a=[]
for i in arr:
    a.append([abs(i-y)]+[i])
a.sort()
a.pop(0)
for i in a[:3]:
    print(i[1],end=' ')
