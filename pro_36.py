n=int(input())
arr=list(map(int,input().split()))
n=len(arr)
count=0
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if arr[i]>arr[j]>arr[k]:
                count+=1
print(count)
