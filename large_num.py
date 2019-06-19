count=int(input())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
res=all(i==arr[0] for i in arr)
if res==True:
    print(arr[0])
else:
    for i in range(len(arr)):
        print(arr[i],end='')
