
n=int(input())
def multiply_matrices(matrix_a, matrix_b):
    n=len(matrix_a)
    result_matrix=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result_matrix[i][j]+=matrix_a[i][k]*matrix_b[k][j]
    return result_matrix

matrix_a=[list(map(int, input().split())) for _ in range(n)]
matrix_b=[list(map(int, input().split())) for _ in range(n)]
result_matrix=multiply_matrices(matrix_a, matrix_b)
for row in result_matrix:
    print(" ".join(map(str, row)))