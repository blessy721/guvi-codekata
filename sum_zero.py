n=int(input())
arr=list(map(int,input().split()))
c=len(arr)
large=max(arr)
y,z=0,0
for i in range(0,c-1):
    for j in range(i+1,c):
        if abs(arr[i]+arr[j])< large:
            y,z=arr[i],arr[j]
            large=abs(y+z)
print(y, z)
