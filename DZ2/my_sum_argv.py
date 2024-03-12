import argparse

def my_sum(*args):
    return sum(args)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('integers', nargs='*', type=float)
    arg = parser.parse_args()
    print(my_sum(*arg.integers))
