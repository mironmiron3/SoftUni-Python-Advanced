countries, capitals = input().split(", "), input().split(", ")
corresponding_info = zip(countries,capitals)
info = {key:value for key,value in corresponding_info}
for pair in info.items():
    print(f"{pair[0]} -> {pair[1]}")