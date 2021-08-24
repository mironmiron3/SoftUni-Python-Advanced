number_of_rows = int(input())
compounds = set()
for i in range(number_of_rows):
    for compound in input().split():
        compounds.add(compound)
[print(item)for item in compounds]