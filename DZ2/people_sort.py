def person_lister(f):
    def inner(people):
        return list(map(f, sorted(people, key=lambda x: x[2])))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    n = int(input())
    if 1 <= n <= 10:
        people = [input().split() for i in range(n)]
        print(*name_format(people), sep='\n')
    else: print("Error!")
