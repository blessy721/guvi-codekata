def weekend(day):
    weekends={"Saturday":1,"Sunday":2}
    if day in weekends:
        print("yes")
    else:
        print("no")


day=str(input())
weekend(day)
