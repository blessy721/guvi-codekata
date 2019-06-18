a=list(map(str,input()))
x=a[0]
y=a[1]
for i in range(len(x)):
    for j in range(len(y)):
        if x[i]==x[j]:
            print("yes")
            break
        else:
            print("no")
