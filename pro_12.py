x, y = map(int,input().split())
arr=list(map(int,input().split()))
ss=[]
for i in range(y):
    a, b = map(int,input().split())
    ss.append([a,b])
sum=0
for i in ss:

    v1=i[0]-1
    v2=i[1]-1
    for j in range(v1,v2+1):
        sum+=arr[j]
    print(sum)
    sum=0
