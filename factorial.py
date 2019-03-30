def factorial(num):
    fact=1
    for i in range(1,num):
        if (num<0):
            print("enter valid number")
        elif num==0:
            print(fact)
        else:
            fact=num*i
            i-=1
            num=fact
    print(fact)

num=int(input())
factorial(num)
