dict = {name: {} for name in input().split(", ")}
command = input()
while not command == "End":
    hero, item, cost = command.split("-")
    if not dict[hero]:
        dict[hero]['items'] = set()
        dict[hero]['cost'] = 0
    if item not in dict[hero]['items']:
        dict[hero]['items'].add(item)
        dict[hero]['cost'] += int(cost)
    command = input()

a = [print(f"{name} -> Items: {len(info['items'])}, Cost: {info['cost']}") for name, info in dict.items()]
