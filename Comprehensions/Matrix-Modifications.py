n = int(input())
matrix = []

for _ in range(n):
    matrix.append(input().split())

matrix = [[int(el) for el in sublist] for sublist in matrix]

command = input()
while not command == "END":

    if command.startswith("Add"):
        useless, row, col, value = command.split()
        row, col, value = int(row), int(col), int(value)
        if 0 <= row <= len(matrix)-1 and 0 <= col <= len(matrix)-1:
            matrix[row][col] += value
        else:
            print("Invalid coordinates")

    elif command.startswith("Subtract"):
        useless, row, col, value = command.split()
        row, col, value = int(row), int(col), int(value)
        if 0 <= row <= len(matrix) - 1 and 0 <= col <= len(matrix) - 1:
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")
    command = input()
#[print(num,end=" ") for sublist in matrix for num in sublist]



for matrix_index in range(len(matrix)):
    matrix[matrix_index] = list(map(str, matrix[matrix_index]))


[print(f"{' '.join(collection)}")for collection in matrix]
a = zip([1,2,3],['a','b'])
print(a)