a, b = input().split()

a,b = int(a), int(b)

set_a = set()
set_b = set()
for i in range(a):
    set_a.add(input())
for m in range(b):
    set_b.add(input())
[print(item)for item in set_a.intersection(set_b)]


