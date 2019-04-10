def countdigits(n):
    count=0
    while n>0:
        n=int(n/10)
        count+=1
    print(count)
n=int(input())
countdigits(n)
