def rev(s):
    words=s.split(" ")
    a=[i[::-1] for i in words]
    ns=(" ".join(a))
    print(ns)

s=str(input())
rev(s)
