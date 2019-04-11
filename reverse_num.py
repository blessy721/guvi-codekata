#reverse of a number
def reverse(n):
    rem=n%10
    n=int(n/10)
    while n>0:
        rem=str(rem)+str(n%10)
        n=int(n/10)
    print(rem)

n=int(input())
reverse(n)
