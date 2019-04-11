def weekend(day):
    weekends={"Saturday":1,"Sunday":2}
    if day in weekends:
        print("Yes")
    else:
        print("No")


day=str(input())
weekend(day)
