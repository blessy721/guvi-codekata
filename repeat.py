def unique_num(count,arr):
    stack=[]
    for i in range(0,count):
        for j in range(i+1,count):
            if arr[i]== arr[j]:
                stack.append(arr[i])

    print(stack[0])

size=int(input())
arr=list(map(int,input().split()))
count=len(arr)
unique_num(count,arr)
