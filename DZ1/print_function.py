n=int(input())
if 1<=n<=20:
    if n<=3:
        print("123",end="")
    else:
        print(123, end="")
        for i in range(4,n+1):
            print(i,end="")    
else:
    print("Error!")
