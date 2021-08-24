rows, cols = [int(el) for el in input().split()]
matrix = []

for row in range(rows):
    matrix.append(input().split())


counter = 0
for r in range(rows-1):
    for c in range(cols-1):
        if matrix[r][c] == matrix[r][c+1] and matrix[r][c+1] == matrix[r+1][c] and matrix[r+1][c] == matrix[r+1][c+1]:
            counter += 1



print(counter)

