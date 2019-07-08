x=int(input())
arr=[]
for i in range(x):
    arr.append(abs(x-(2**i)))
arr.sort()
print(arr[0])
