x, y=map(int,input().split())
one=list(map(int,input().split()))
sec=list(map(int,input().split()))
for i in range(len(sec)):
    one.append(sec[i])
    one.sort()
    print(one[-1],end=' ')
    i=i+1
