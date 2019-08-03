n=int(input())
arr=list(map(int,input().split()))
count=0
if len(arr)==1:
    print(1)
else:
    for i in range(1,len(arr)-1):
        if (arr[i]<arr[i-1] and arr[i]<arr[i+1]) or (arr[i]>arr[i-1] and arr[i]>arr[i+1]):
            count+=1
    print(count)
