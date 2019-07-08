import statistics as st
count=int(input())
arr=list(map(int,input().split()))
yes=False
for i in range(1,count):
    l1=arr[:i]
    l2=arr[i:]
    if st.mean(l1)==st.mean(l2):
        yes=True
if yes==True:
    print("yes")
else:
    print("no")
