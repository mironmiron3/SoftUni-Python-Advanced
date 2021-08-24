list_of_names = input().split(", ")
[print(f"{word} -> {len(word)}",end=", ") if word != list_of_names[-1] else print(f"{word} -> {len(word)}") for word in list_of_names]