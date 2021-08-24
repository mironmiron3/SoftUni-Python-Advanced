from pprint import pprint
n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(el) for el in input().split()])


explosion_coordinates = input().split(" ")
for pair in explosion_coordinates:
    row,col = [int(coordinate) for coordinate in pair.split(",")]
    if matrix[row][col] > 0:
        potential_targets = [(row-1,col-1),(row-1,col),(row-1,col+1),(row,col-1),(row,col+1),(row+1,col-1),(row+1,col),(row+1,col+1)]
        for tup in potential_targets:
            target_row,target_col = tup
            if 0 <= target_row < n and 0 <= target_col < n:
                if matrix[target_row][target_col] > 0:
                    matrix[target_row][target_col] -= matrix[row][col]
        matrix[row][col] = 0

sum = 0
alive_cells_count = 0
for sublist in matrix:
    for num in sublist:
        if num > 0:
            alive_cells_count += 1
            sum += num
print(f"Alive cells: {alive_cells_count}")
print(f"Sum: {sum}")
[print(" ".join([str(el) for el in element])) for element in matrix]

#print(matrix)


