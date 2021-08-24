import sys

rows, cols = [int(el) for el in input().split()]
matrix = []
for row in range(rows):
    matrix.append([int(el) for el in input().split()])

max_sum = -sys.maxsize
max_index = None

for r in range(rows-2):
    for c in range(cols-2):
        current_sum = matrix[r][c] + matrix[r][c+1] + matrix[r][c+2] + matrix[r+1][c] + matrix[r+1][c+1] + matrix[r+1][c+2]+ matrix[r+2][c] + matrix[r+2][c+1]+ matrix[r+2][c+2]
        if current_sum > max_sum:
            max_sum = current_sum
            max_index = (r,c)
row,col = max_index
print(f"Sum = {max_sum}")
print(f"{matrix[row][col]} {matrix[row][col+1]} {matrix[row][col+2]}")
print(f"{matrix[row+1][col]} {matrix[row+1][col+1]} {matrix[row+1][col+2]}")
print(f"{matrix[row+2][col]} {matrix[row+2][col+1]} {matrix[row+2][col+2]}")
