from collections import deque

chocolates = [int(el) for el in input().split(", ")]
milks = deque([int(el) for el in input().split(", ")])

total_shakes = 0
is_completed = False
while True:
    if total_shakes == 5:
        is_completed = True
        break
    if not chocolates:
        break
    if not milks:
        break
    current_chocolate = chocolates[len(chocolates)-1]
    current_milk = milks[0]
    if current_chocolate <= 0 or current_milk <= 0:
        if current_milk <= 0:
            milks.popleft()
        if current_chocolate <= 0:
            chocolates.pop()

        continue

    if current_milk == current_chocolate:
        chocolates.pop()
        milks.popleft()
        total_shakes += 1
    else:
        milks.append(milks.popleft())
        chocolates[len(chocolates)-1] -= 5


if is_completed:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join([str(integ) for integ in chocolates])}")
else:
    print(f"Chocolate: empty")
if milks:
    print(f"Milk: {', '.join([str(integ) for integ in milks])}")
else:
    print("Milk: empty")