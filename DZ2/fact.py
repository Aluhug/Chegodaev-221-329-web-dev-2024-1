import sys, time

def fact_rec(n):
    if n == 1:
        return 1
    return fact_rec(n - 1) * n

def fact_it(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(fact_it(50))
if __name__ == '__main__':
    sys.setrecursionlimit(5000)
    start_time_rec = time.time()
    fact_rec(2000)
    end_time_rec = time.time()

    start_time_it = time.time()
    fact_it(2000)
    end_time_it = time.time()
    print(
        f"Recursion time: {format(end_time_rec - start_time_rec, '.3f')}; \n"
        f"Iteration time: {format(end_time_it - start_time_it, '.3f')};")
        # Recursion time: 0.009; 
        # Iteration time: 0.003;