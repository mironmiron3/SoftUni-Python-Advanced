nums = tuple([float(element) for element in input().split()])
dict = {}
for num in nums:
    if num not in dict:
        dict[num] = 0
    dict[num] += 1
[print(f"{key} - {value} times") for key, value in sorted(dict.items(), key=lambda kvp:kvp[0])]