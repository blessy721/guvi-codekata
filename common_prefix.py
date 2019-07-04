
def com_pre_1(n,arr):
    minlen=com_pre(n,arr)
    res=""
    for i in range(minlen):
        curr=arr[0][i]
        for j in range(1,n):
            if arr[j][i]!=curr:
                return res
        res += curr
    return res
def com_pre(n,arr):
    pref=len(arr[0])
    for i in range(1,n):
        if (len(arr[i]) < pref):
            pref=len(arr[i])
    return pref

n=int(input())
arr=[]
for i in range(n):
    arr.append(input())
ans=com_pre_1(n,arr)
print(ans)
