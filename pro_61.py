import string
alpha=list(string.ascii_lowercase)
s1=list(input())
s2=list(input())
for i in range(len(s1)):
    key=alpha.index(s1[i]) + alpha.index(s2[i]) + 1
    if key<25:
        print(alpha[key],end='')
    else:
        print(alpha[key-26],end='')
