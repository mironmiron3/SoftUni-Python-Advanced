phones = {}
data = input()
while not data.isdigit():
    name, phone = data.split("-")
    phones[name] = phone
    data = input()
data = int(data)
for i in range(data):
    searched_name = input()
    if searched_name not in phones:
        print(f"Contact {searched_name} does not exist.")

        continue
    print(f"{searched_name} -> {phones[searched_name]}")