n = int(input())
matrix = []
for _ in range(n):
    matrix.append(input().split(", "))

primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = []
for i in range(n):
    for j in range(n):
        if i + j == n -1:
            secondary_diagonal.append(matrix[i][j])
sum_of_primary = sum([int(el) for el in primary_diagonal])
sum_of_secondary = sum([int(el) for el in secondary_diagonal])
print(f"First diagonal: {', '.join(primary_diagonal)}. Sum: {sum_of_primary}")
print(f"Second diagonal: {', '.join(secondary_diagonal)}. Sum: {sum_of_secondary}")