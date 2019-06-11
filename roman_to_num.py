global romn_dict
romn_dict={"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000}
def conv(arr):
    for i in arr:
        print(romn_dict[i])

arr=list(input().split())
conv(arr)
