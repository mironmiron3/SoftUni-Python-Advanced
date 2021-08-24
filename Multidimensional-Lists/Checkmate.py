def can_defeat_a_king(example_matrix,j,k):
    new_sublist_index,new_item_index = j - 1, k

    while new_sublist_index in range(len(example_matrix)) and new_item_index in range(len(example_matrix[new_sublist_index])):

        if example_matrix[new_sublist_index][new_item_index] == "Q":
            break
        elif example_matrix[new_sublist_index][new_item_index] == "K":
            return True
        new_sublist_index -= 1
    new_sublist_index, new_item_index = j+1, k
    while new_sublist_index in range(len(example_matrix)) and new_item_index in range(len(example_matrix[new_sublist_index])):

        if example_matrix[new_sublist_index][new_item_index] == "Q":
            break
        elif example_matrix[new_sublist_index][new_item_index] == "K":
            return True
        new_sublist_index += 1
    new_sublist_index, new_item_index = j, k+1
    while new_sublist_index in range(len(example_matrix)) and new_item_index in range(len(example_matrix[new_sublist_index])):

        if example_matrix[new_sublist_index][new_item_index] == "Q":
            break
        elif example_matrix[new_sublist_index][new_item_index] == "K":
            return True
        new_item_index += 1
    new_sublist_index, new_item_index = j, k-1
    while new_sublist_index in range(len(example_matrix)) and new_item_index in range(len(example_matrix[new_sublist_index])):

        if example_matrix[new_sublist_index][new_item_index] == "Q":
            break
        elif example_matrix[new_sublist_index][new_item_index] == "K":
            return True
        new_item_index -= 1
    new_sublist_index,new_item_index = j-1,k-1
    while new_sublist_index in range(len(example_matrix)) and new_item_index in range(len(example_matrix[new_sublist_index])):

        if example_matrix[new_sublist_index][new_item_index] == "Q":
            break
        elif example_matrix[new_sublist_index][new_item_index] == "K":
            return True
        new_item_index -= 1
        new_sublist_index -= 1
    new_sublist_index,new_item_index = j+1,k+1
    while new_sublist_index in range(len(example_matrix)) and new_item_index in range(len(example_matrix[new_sublist_index])):

        if example_matrix[new_sublist_index][new_item_index] == "Q":
            break
        elif example_matrix[new_sublist_index][new_item_index] == "K":
            return True
        new_item_index += 1
        new_sublist_index += 1
    new_sublist_index,new_item_index = j-1,k+1
    while new_sublist_index in range(len(example_matrix)) and new_item_index in range(len(example_matrix[new_sublist_index])):

        if example_matrix[new_sublist_index][new_item_index] == "Q":
            break
        elif example_matrix[new_sublist_index][new_item_index] == "K":
            return True
        new_item_index += 1
        new_sublist_index -= 1
    new_sublist_index, new_item_index = j + 1, k - 1
    while new_sublist_index in range(len(example_matrix)) and new_item_index in range(
            len(example_matrix[new_sublist_index])):

        if example_matrix[new_sublist_index][new_item_index] == "Q":
            break
        elif example_matrix[new_sublist_index][new_item_index] == "K":
            return True
        new_item_index -= 1
        new_sublist_index += 1





matrix = []
king_defeated = False


for i in range(8):
    matrix.append(input().split())
for j in range(len(matrix)):
    for k in range(len(matrix[j])):
        if matrix[j][k] == "Q":
            if can_defeat_a_king(matrix,j,k):
                print([j,k])
                king_defeated = True
if not king_defeated:
    print("The king is safe!")