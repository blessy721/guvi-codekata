a=list(map(str,input().split()))
s=a[0]
char=a[1]
for i in range(len(s)):
    if s[i]==char:
        print(i+1)
        break
