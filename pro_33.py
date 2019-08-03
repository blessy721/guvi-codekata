s=input()
first=s[0]
for i in range(1,len(s)):
    if s[i]>first:
        p=s[i:]
print(p)
