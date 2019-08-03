s=input()
res=True
for i in s:
    if i not in "dhoni":
        res=False
print('yes'if res==True else 'no')
