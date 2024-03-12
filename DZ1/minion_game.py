s=input().strip().upper()
k_score=0
s_score=0

glasnie="AEIOU"

for i in range(len(s)):
    if s[i] in glasnie:
        k_score+=len(s)-i
    else:
        s_score+=len(s)-i
        
if k_score>s_score:
    print(f"Kevin {k_score}")
elif k_score<s_score:
    print(f"Stuart {s_score}")
else:
    print("Ничья!")