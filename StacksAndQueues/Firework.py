from collections import deque
firework_effects = deque([int(el) for el in input().split(", ") if int(el) > 0])
explosive_powers = [int(num) for num in input().split(", ") if int(num) > 0]
palms = 0
willows = 0
crossettes = 0
ready_with_fireworks = False
while not ready_with_fireworks:
    if not firework_effects or not explosive_powers:
        break
    current_firework = firework_effects.popleft()
    current_power = explosive_powers.pop()
    sum = current_power + current_firework
    if sum % 3 == 0 and sum % 5 == 0:
        crossettes += 1
    elif sum % 3 == 0:
        palms += 1
    elif sum % 5 == 0:
        willows += 1
    elif not sum % 3 == 0 and not sum % 5 == 0:
        current_firework -= 1
        firework_effects.append(current_firework)
        explosive_powers.insert(0,current_power)
    if crossettes == 3 and willows == 3 and palms == 3:
        ready_with_fireworks = True

if ready_with_fireworks:
    print(f"Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can't make the perfect firework show.")
print(f"Firework Effects left: {firework_effects}")
print(f" Explosive Power left: {explosive_powers}")
print(palms)
print(willows)
print(crossettes)