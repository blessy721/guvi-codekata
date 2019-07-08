x, y = map(int,input().split())
arr=list(map(int,input().split()))
ss=[]
arr.insert(0,0)
for i in range(y):
    xor=0
    a, b = map(int,input().split())
    for i in range(a,b+1):
        xor^=arr[i]
    ss.append(xor)

for i in ss:
    print(i)
