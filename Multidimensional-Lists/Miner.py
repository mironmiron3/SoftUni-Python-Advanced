import sys
def moving_to(matrix,row,col):
    if matrix[row][col] == "c":
        return "coal"
    elif matrix[row][col] == "*":
        return "regular"
    elif matrix[row][col] == "e":
        return "end"

n = int(input())

list_of_commands = input().split()
matrix = []
for _ in range(n):
    matrix.append(input().split())
coal_count = 0
start_coordinates = None
for row in matrix:
    for col in row:
        if col == "c":
            coal_count += 1
        elif col == "s":
            start_coordinates = (matrix.index(row), row.index(col))

current_row, current_col = map(int,start_coordinates)

is_ended_unsuccessfully = False

for command in list_of_commands:


    if command == "up":
        if 0 <= current_row - 1 < n:
            current_row = current_row - 1
            if moving_to(matrix,current_row,current_col) == "coal":
                coal_count -= 1
                matrix[current_row][current_col] = "*"
            elif moving_to(matrix,current_row,current_col) == "end":
                is_ended_unsuccessfully = True
                print(f"Game over! ({current_row}, {current_col})")
                break


    elif command == "down":
        if 0 <= current_row + 1 < n:
            current_row = current_row + 1
            if moving_to(matrix,current_row,current_col) == "coal":
                coal_count -= 1
                matrix[current_row][current_col] = "*"
            elif moving_to(matrix,current_row,current_col) == "end":
                is_ended_unsuccessfully = True
                print(f"Game over! ({current_row}, {current_col})")
                break

    elif command == "right":
        if 0 <= current_col + 1 < n:
            current_col = current_col + 1
            if moving_to(matrix,current_row,current_col) == "coal":
                coal_count -= 1
                matrix[current_row][current_col] = "*"
            elif moving_to(matrix,current_row,current_col) == "end":
                is_ended_unsuccessfully = True
                print(f"Game over! ({current_row}, {current_col})")
                break

    elif command == "left":
        if 0 <= current_col - 1 < n:
            current_col = current_col - 1
            if moving_to(matrix,current_row,current_col) == "coal":
                coal_count -= 1
                matrix[current_row][current_col] = "*"
            elif moving_to(matrix,current_row,current_col) == "end":
                is_ended_unsuccessfully = True
                print(f"Game over! ({current_row}, {current_col})")
                break

    if coal_count == 0:
        print(f"You collected all coals! ({current_row}, {current_col})")
        sys.exit()


if not is_ended_unsuccessfully:
    print(f"{coal_count} coals left. ({current_row}, {current_col})")