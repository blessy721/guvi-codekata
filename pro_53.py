import string
st=input()
st.lower()
res=True
alpha=list(string.ascii_lowercase)
for i in alpha:
    if i not in st:
        res=False
        break
if res==True:
    print('yes')
else:
    print('no')
