n=int(input())
arr=list(map(int,input().split()))
c=len(arr)
large=max(arr)
for i in range(0,c-1):
    for j in range(0,c):
        if abs(arr[i]+arr[j])< large:
            y,z=arr[i],arr[j]
            large=abs(y+z)
print(y, z)
