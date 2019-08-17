arr=list(input())
longest_common=0
for i in range(len(arr)):
    temp=arr[i:]
    rev=list(reversed(temp))
    if temp==rev:
        if longest_common<len(rev):
            longest_common=len(rev)
for i in range(len(arr)):
    temp=arr[:len(arr)-i]
    rev=list(reversed(temp))
    if temp==rev:
        if longest_common<len(rev):
            longest_common=len(rev)
print(len(arr)-longest_common)
