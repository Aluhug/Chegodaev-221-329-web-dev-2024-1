s=input()
new_s=""
if 0<len(s)<=1000:
    for x in s:
        if x.isupper():
            new_s+=x.lower()
        else:
            new_s+=x.upper()
    print(new_s)
else:
    print("Error!")