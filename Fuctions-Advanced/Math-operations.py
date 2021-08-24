def math_operations(*numbers, **kwargs):
    mapper = {1:"a", 2:"s", 3:"d", 4:"m"}
    turn = 1
    for i in range(len(numbers)):
        if turn == 5:
            turn = 1
        if turn == 1:
            kwargs[mapper[turn]] += numbers[i]
        elif turn == 2:
            kwargs[mapper[turn]] -= numbers[i]
        elif turn == 3:
            if not numbers[i] == 0:
                kwargs[mapper[turn]] /= numbers[i]
        elif turn == 4:
            kwargs[mapper[turn]] *= numbers[i]
        turn += 1
    return kwargs
print(math_operations(6, a=0, s=0, d=0, m=0))

