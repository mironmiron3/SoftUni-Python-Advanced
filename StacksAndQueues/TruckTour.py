from collections import deque
n = int(input())
gas_pumps = deque()
for i in range(n):
    gas_pump = input().split()
    gas_pumps.append(gas_pump)

for i in range(len(gas_pumps)):
    total_liters_available = 0
    is_doable = True
    for pump in gas_pumps:
        total_liters_available += int(pump[0])
        if total_liters_available < int(pump[1]):
            is_doable = False
            break
        total_liters_available -= int(pump[1])
    if is_doable:
        print(i)
        break

    gas_pumps.rotate(-1)

