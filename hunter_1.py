def unique(arr,count):
    stack=[]
    for i in range(0,count):
        for j in range(i+1,count):
            if arr[i]==arr[j]:
                if arr[i] not in stack:
                    stack.append(arr[i])
    if (len(stack)>0):
        for i in range(len(stack)):
            print(stack[i],end=' ')
    else:
        print("Unique")


arr=[1,2,3,3,2,3,4,3]
count=len(arr)
unique(arr,count)
