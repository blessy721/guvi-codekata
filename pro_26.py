def LIS(arr,size):
    res=[]
    count=1
    for i in arr:
        if i not in res:
            res.append(i)
    for i in range(len(res)-1):
        if res[i]<res[i+1]:
            count+=1
    print(count)
size=int(input())
arr=list(map(int,input().split()))
LIS(arr,size)
