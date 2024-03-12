import math, random

def circle_square_mk(a, b):
    i = 0
    cnt = 0
    while i < b:
        x = random.random()
        y = random.random()
        if ((x**2) + (y**2)) <= 1:
            cnt += 1
        i += 1
    return (4 * (cnt / b) * (a**2))

if __name__ == '__main__':
    a, b = map(float, input().split())
    for i in range(20):
        print(circle_square_mk(a, b))

'''
Тесты:
При b = 10 диапазон значений: от 2.4 до 4.0. Разница 1.6
При b = 50 диапазон значений: от 2.8 до 3.44. Разница 0.64
При b = 100 диапазон значений: от 3.0 до 3.36. Разница 0.36
При b = 500 диапазон значений: от 3.016 до 3.232. Разница 0.216
При b = 10000 диапазон значений: от 3.116 до 3.1648. Разница 0.0532
'''
