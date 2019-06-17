a=[]
for i in range(3):
    a.append(list(map(int,input().split())))
first=a[0]
second=a[1]
third=a[2]
if first[0]==second[0] and second[0]==third[0]:
    print("yes")
elif first[1]==second[1] and second[1]==third[1]:
    print("yes")
else:
    print("no")
