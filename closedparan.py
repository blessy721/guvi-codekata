def process(str):
    open=["[","(","{"]
    closed=["]",")","}"]
    stack=[]
    for i in str:
        if i in open:
            stack.append(i)
        elif i in closed:
            loc=closed.index(i)
            if (len(stack)>0) and (open[loc]==(stack[len(stack)-1])):
                stack.pop()
            else:
                print("no")
    if len(stack)==0:
        print("yes")
str=str(input())
process(str)
