n=int(input())
if 2<=n<=5:
    students=[]

    for _ in range(n):
        name = input()
        mark = float(input())
        student = [name, mark]
        students.append(student)

    students.sort(key=lambda x: (x[1], x[0]))

    second_max_mark = sorted(set(mark for name, mark in students))[1]

    for name, mark in students:
        if mark == second_max_mark:
            print(name)
else:
    print("Error!")