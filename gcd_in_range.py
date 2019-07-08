import math
x, y = map(int,input().split())
lis=[]
arr=list(map(int,input().split()))
for i in range(y):
    a,b=map(int,input().split())
    lis.append([a,b])
for i in lis:
    v1=i[0]-1
    v2=i[1]-1
    print(math.gcd(arr[v1],arr[v2]))
