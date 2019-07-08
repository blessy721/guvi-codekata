x, y = map(int,input().split())
arr=list(map(int,input().split()))
ss=[]
for i in range(y):
    a, b = map(int,input().split())
    ss.append([a,b])
tem=[]
for i in ss:
    v1=i[0]-1
    v2=i[1]
    for i in arr[v1:v2]:
        tem.append(i)
    print(min(tem))
    tem=[]
