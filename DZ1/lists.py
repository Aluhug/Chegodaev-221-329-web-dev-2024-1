n=int(input())
arr=[]

for _ in range(n):
    x=input().split()
    
    if x[0]=="insert":
        i,e=map(int,x[1:])
        arr.insert(i,e)
    elif x[0]=="print":
        print(arr)
    elif x[0]=="remove":
        e=int(x[1])
        arr.remove(e)
    elif x[0]=="append":
        e=int(x[1])
        arr.append(e)
    elif x[0]=="sort":
        arr.sort()
    elif x[0]=="pop":
        arr.pop()
    elif x[0]=="reverse":
        arr.reverse()
    else:
        print("Error!")