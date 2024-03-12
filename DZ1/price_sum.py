prices = [0, 0, 0]
n=input()
with open(n, "r", encoding="utf-8") as file:
    for x in file:
        if x=='':
            continue
        pname, aprice, pprice, cprice = x.strip().split(",")
        if pname=="Продукт":
            continue
        prices[0] += float(aprice)
        prices[1] += float(pprice)
        prices[2] += float(cprice)

result="""{:.2f} {:.2f} {:.2f}"""
print(result.format(*prices))