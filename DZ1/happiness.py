n, m = map(int, input().split())
arr = list(map(int, input().split()))
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

happiness = 0

if 1<=n<=10**5 and 1<=n<=10**5 and 1<=m<=10**5:
    for num in arr:
        if num in setA:
            happiness += 1
        elif num in setB:
            happiness -= 1

    print(happiness)
else:
    print("Error!")