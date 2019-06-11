def unique(arr,count):
    stack=[]
    for i in range(0,count):
        if i==arr[i]:
            if arr[i] not in stack:
                stack.append(arr[i])
    if len(stack)>0:
        stack.sort()
        for i in range(len(stack)):
            print(stack[i],end=' ')
    else:
        print("-1")
size=int(input())
arr=list(map(int,input().split()))
count=len(arr)
unique(arr,count)
