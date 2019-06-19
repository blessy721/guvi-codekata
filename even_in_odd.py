def even_odd(n,arr):
    s=[]
    for i in range(0,n):
        if arr[i]%2==0:
            if i%2==1:
                s.append(arr[i])
                i+=1
        elif arr[i]%2==1:
            if i%2==0:
                s.append(arr[i])
                i+=1
    for i in s:
        print(i,end=' ')

size=int(input())
arr=list(map(int,input().split()))
n=len(arr)
even_odd(n,arr)
