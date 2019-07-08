size=int(input())
count=0
arr=list(map(int,input().split()))
for a in range(0,size-2):
    for b in range(1,size-1):
        for c in range(2,size):
            if (arr[a]<arr[b] and arr[b]<arr[c]):
                count+=1
print(count)
