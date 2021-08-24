info = input().split("|")
#a = [int(num) for group in info for num in group.split()]
a = [sorted(map(int,group.split())) for group in reversed(info)]
print(a)
a = [str(item) for sub in a for item in sub]
#print(' '.join([item for subgroup in a for item in subgroup]))
print(' '.join(a))