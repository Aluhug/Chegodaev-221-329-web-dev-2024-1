n, m=map(int, input().split())
items=[]

def capacity_func(capacity, items):
    items.sort(key=lambda x: x[2] / x[1], reverse=True)
    selected_items=[]
    total_weight=0

    for item in items:
        if total_weight+item[1]<=capacity:
            selected_items.append(item)
            total_weight+=item[1]
        else:
            fraction=(capacity-total_weight)/item[1]
            selected_items.append((item[0], item[1]*fraction, item[2]*fraction))
            break
    return selected_items

for _ in range(m):
    cargo_name, weight, value=input().split()
    weight, value=int(weight), int(value)
    items.append((cargo_name, weight, value))

selected_cargo=capacity_func(n, items)
for cargo in selected_cargo:
    print(f"{cargo[0]} {cargo[1]:.2f} {cargo[2]}", flush=True)
