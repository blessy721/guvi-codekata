from itertools import combinations
(num, x) =input().split()
x=int(x)
arr=[]
comb=combinations(num,len(num)-x)
comb=list(comb)
#print(comb)
for i in (comb):
    arr.append("".join(i))
#print(arr)
print(min(arr))
#for i in list(comb):
#    arr.append()
