a=list(map(int,input().split()))
count=a[0]
s=a[1]
b=list(map(int,input().split()))
for i in range(len(b)):
    for j in range(i+1,len(b)):
        if b[i]+b[j]==s:
            print('yes')
            break
