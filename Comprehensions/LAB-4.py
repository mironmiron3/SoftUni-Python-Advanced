n = int(input())

matrix = [[int(element) for element in input().split(", ") if int(element) % 2 == 0]for _ in range(n)]
print(matrix)