def prime(first,last):
    global l
    l=[]
    for i in range(first,last+1):
        if i > 1:
            for d in range(2,i):
                if (i%d)==0:
                    break
                else:
                    print(i)



(first, last) = map(int,input().split())
print(first)
print(last)
prime(first,last)
