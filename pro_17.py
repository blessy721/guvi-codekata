x,y = map(int,input().split())
arr=list(map(int,input().split()))
tem=False
for i in range(0,x):
    for j in range(i+1,x):
        if arr[i]+arr[j]==y:
            tem=True
if tem==True:
    print("yes")
else:
    print("no")
