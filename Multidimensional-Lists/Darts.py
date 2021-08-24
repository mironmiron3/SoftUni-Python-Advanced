first_player, second_player = input().split(", ")

info = {first_player: {"points": 501, "throws": 0}, second_player: {"points": 501, "throws": 0}}


matrix = []
for _ in range(7):
    matrix.append(input().split())

somebody_won = False

all_throws = 0
while not somebody_won:

    data = input()
    row, col = int(data[1]), int(data[4])
    all_throws += 1
    current_player = None
    if all_throws % 2 == 0:
        info[second_player]["throws"] += 1
        current_player = second_player
    else:
        info[first_player]["throws"] += 1
        current_player = first_player
    if matrix[row][col] == "B":
        print(f"{current_player} won the game with {info[current_player]['throws']} throws!")
        somebody_won = True
    elif matrix[row][col] == "D":
        points = (int(matrix[row][0]) + int(matrix[row][6]) + int(matrix[0][col]) + int(matrix[6][col])) * 2
        info[current_player]["points"] -= points
    elif matrix[row][col] == "T":
        points = (int(matrix[row][0]) + int(matrix[row][6]) + int(matrix[0][col]) + int(matrix[6][col])) * 3
        info[current_player]["points"] -= points
    elif matrix[row][col].isdigit():
        info[current_player]["points"] -= int(matrix[row][col])
    if info[current_player]["points"] <= 0:
        print(f"{current_player} won the game with {info[current_player]['throws']} throws!")
        somebody_won = True







