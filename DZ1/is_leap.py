year=int(input())
if 1900<=year<=10**5:
    if (year%4==0 and year%100!=0) or (year%400==0):
        print("True")
    else:
        print("False") 
else:
    print("Error!")