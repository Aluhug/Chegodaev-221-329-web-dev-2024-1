n=int(input())
A=list(map(int, input().split()))
maxs=max(A)
A = [i for i in A if i != maxs]
maxs2=max(A)
print(maxs2)