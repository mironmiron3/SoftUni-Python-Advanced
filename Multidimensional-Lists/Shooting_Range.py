def is_valid(row,col,distance,direction):
    position = [row,col]
    if direction == "up":
        position[0] -= distance
    elif direction == "down":
        position[0] += distance
    elif direction == "right":
        position[1] += distance
    elif direction == "left":
        position[1] -= distance
    if 0 <= position[0] < 5 and 0 <= position[1] < 5:
        return position
    return False
matrix = []
for _ in range(5):
    matrix.append(input().split())

current_position = []
all_targets = []

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == "A":
            current_position.extend([row,col])
        if matrix[row][col] == "x":
            all_targets.append((row,col))
all_targets_count = len(all_targets)
targets_hit = []
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == "move":
        direction = command[1]
        distance = int(command[2])
        if is_valid(current_position[0],current_position[1],distance, direction) and matrix[is_valid(current_position[0],current_position[1],distance, direction)[0]][is_valid(current_position[0],current_position[1],distance, direction)[1]] == ".":
            matrix[current_position[0]][current_position[1]] = "."
            current_position = is_valid(current_position[0],current_position[1],distance, direction)
            matrix[current_position[0]][current_position[1]] = "A"
    if command[0] == "shoot":
        direction = command[1]
        if direction == "up":
            for i in range(current_position[0]-1,-1,-1):
                if matrix[i][current_position[1]] == "x":
                    targets_hit.append((i,current_position[1]))
                    matrix[i][current_position[1]] = "."
                    break
        if direction == "down":
            for i in range(current_position[0]+1,5):
                if matrix[i][current_position[1]] == "x":
                    targets_hit.append((i,current_position[1]))
                    matrix[i][current_position[1]] = "."
                    break
        if direction == "right":
            for i in range(current_position[1]+1,5):
                if matrix[current_position[0]][i] == "x":
                    targets_hit.append((current_position[0],i))
                    matrix[current_position[0]][i] = "."
                    break
        if direction == "left":
            for i in range(current_position[1]-1,-1,-1):
                if matrix[current_position[0]][i] == "x":
                    targets_hit.append((current_position[0],i))
                    matrix[current_position[0]][i] = "."
                    break

if all_targets_count == len(targets_hit):
    print(f"Training completed! All {all_targets_count} targets hit.")
else:
    print(f"Training not completed! {all_targets_count-len(targets_hit)} targets left.")
[print([tup[0],tup[1]]) for tup in targets_hit]


