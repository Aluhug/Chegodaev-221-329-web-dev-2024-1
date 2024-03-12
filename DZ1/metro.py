n=int(input())
passengers_times=[]
for _ in range(n):
    entry, exit = map(int, input().split())
    passengers_times.append((entry, exit))

t=int(input())

tpeople = sum(1 for entry, exit in passengers_times if entry<=t<=exit)
print(tpeople)