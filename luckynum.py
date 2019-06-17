def lucky(N,arr):
    count=0
    for i in range(0,len(arr)):
        if (N*(i+1)) in arr:
            count+=1
    print(count)
N=int(input())
arr=list(map(int,input().split()))
lucky(N,arr)
