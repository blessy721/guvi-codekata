def permm(n):
    lis=[]
    if len(n)==0:
        return []
    if len(n)==1:
        return [n]
    for i in range(len(n)):
        a=n[i]
        rem = n[:i]+n[i+1:]
        for p in permm(rem):
            lis.append([a]+p)
    return lis
n=list(input())
for i in permm(n):
    print("".join(i))
