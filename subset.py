def subset(arr_a,arr_b):
    for i in arr_a:
        for j in arr_b:
            if i == j:
                arr_b.pop(arr_b.index(j))
    if len(arr_b)>0:
        print("NO")
    else:
        print("YES")

num=list(map(int,input().split()))
arr_a=list(map(int,input().split()))
arr_b=list(map(int,input().split()))
arr_a.sort()
arr_b.sort()
print(arr_a)
print(arr_b)
subset(arr_a,arr_b)
