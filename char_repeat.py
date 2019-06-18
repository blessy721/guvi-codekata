a=list(map(str,input().split()))
s=a[0]
char=a[1]
count=0
for i in range(len(s)):
    if s[i]==char:
        count+=1
print(count)
