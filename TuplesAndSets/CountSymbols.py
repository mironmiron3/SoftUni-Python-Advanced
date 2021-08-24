string = input()
characters = {}
for char in string:
    if char not in characters:
        characters[char] = 0
    characters[char] += 1
[print(f"{character}: {times} time/s") for character, times in sorted(characters.items(), key= lambda kvp:kvp[0])]