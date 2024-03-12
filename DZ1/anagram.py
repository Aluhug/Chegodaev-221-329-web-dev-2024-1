s1 = input()
s2 = input()

def anagrama(s1, s2):
    return sorted(s1)==sorted(s2)
if anagrama(s1, s2):
    print("YES")
else:
    print("NO")