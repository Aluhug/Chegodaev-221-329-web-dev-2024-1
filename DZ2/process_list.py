import sys, time

def process_list(arr):
    if len(arr) < 1 or len(arr) > 10 ** 3:
        return "Error!"
    else:
        result = []
        for i in arr:
            if i % 2 == 0:
                result.append(i ** 2)
            else:
                result.append(i ** 3)

        else:
            return result

def process_list_gen(arr):
    return [i ** 2 if i % 2 == 0 else i ** 3 for i in arr]

if __name__ == '__main__':
    example_arr = [i for i in range(10000)]
    start_time = time.time()
    process_list(example_arr)
    end_time = time.time()

    start_time_gen = time.time()
    process_list_gen(example_arr)
    end_time_gen = time.time()
    print(
        f"First time {format(end_time - start_time, '.5f')}\n"
        f"Gen time {format(end_time_gen - start_time_gen, '.5f')}")
    # First time 0.00000
    # Gen time 0.0400
