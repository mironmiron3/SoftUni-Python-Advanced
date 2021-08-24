n = int(input())
matrix = []

for row in range(n):
    matrix.append([int(el) for el in input().split()])

primary_diagonal = 0
secondary_diagonal = 0

for i in range(n):
    primary_diagonal += matrix[i][i]

counter = 0
for m in range(n-1,-1,-1):
    secondary_diagonal += matrix[counter][m]
    counter += 1

print(abs(primary_diagonal-secondary_diagonal))