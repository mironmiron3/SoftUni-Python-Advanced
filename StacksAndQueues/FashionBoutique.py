clothes = [int(piece) for piece in input().split()]
initial_rack_capacity = int(input())
number_of_racks = 1
rack_capacity = initial_rack_capacity
while clothes:
    current_piece = clothes.pop()
    if current_piece > rack_capacity:
        number_of_racks += 1
        rack_capacity = initial_rack_capacity - current_piece
    else:
        rack_capacity -= current_piece
print(number_of_racks)