rows, columns = input().split()
rows, columns = int(rows), int(columns)

for i in range(rows):

    result = [(chr(97+i),chr(97+j+i),chr(97+i)) for j in range(columns)]
    [print(''.join(tup),end=" ") for tup in result]
    print()