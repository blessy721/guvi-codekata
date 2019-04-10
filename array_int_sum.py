def func(arr,n,k):
    sum=0
    for i in (range(k)):
        sum=sum+int(arr[i])
    print(sum)
n=list(input().split())
n=n[0]
k=int(n[1])
arr=list(input())
func(arr,n,k)
