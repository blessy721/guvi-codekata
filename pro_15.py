n=int(input())
arr=list(map(int,input().split()))
ss=list(map(bin,arr))
a=sorted(ss,reverse = True)
for i in a:
    print(int(i,2))
