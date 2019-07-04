
def com_pre_1(s1,s2):
    n1=len(s1)
    n2=len(s2)
    result=""
    i=0
    j=0
    while i<=n1-1 and j<=n2-1:
        if s1[i]!=s2[j]:
            break
        result+=s1[i]
        i+=1
        j+=1
    return result
def com_pre(n,arr):
    pref=arr[0]
    for i in range(1,n):
        prefix=com_pre_1(pref,arr[i])
    return prefix

n=int(input())
arr=[]
for i in range(n):
    arr.append(input())
ans=com_pre(n,arr)
print(ans)
