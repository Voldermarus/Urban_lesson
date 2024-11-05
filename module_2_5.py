def get_matrix(n, m, value):
    matrix = []

    for i in range(n):
        row = [value]
        row.append(value)
        matrix.append(row)

    for j in range(m):

        return matrix

result = get_matrix(2, 2, 10)
print(result)

result = get_matrix(3, 5, 42)
print(result)

result = get_matrix(4, 2, 13)
print(result)