count=int(input())
arr=[]
ss=[]
for i in range(count):
    arr.append(list(map(int,input().split())))
for llist in arr:
    for num in llist:
        ss.append(num)
ss.sort()
for i in ss:
    print(i,end=' ')
