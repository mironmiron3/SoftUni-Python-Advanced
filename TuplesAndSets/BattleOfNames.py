n = int(input())
set_even = set()
set_odd = set()

for i in range(1, n+1):
    name = input()
    sum = 0
    for char in name:
        sum += ord(char)
    sum = sum // i
    if sum % 2 == 0:
        set_even.add(sum)
    else:
        set_odd.add(sum)
sum_even = 0
for number in set_even:
    sum_even += number
sum_odd = 0
for number1 in set_odd:
    sum_odd += number1
if sum_odd == sum_even:
    print(", ".join([str(x) for x in set_even.union(set_odd)]))
if sum_odd > sum_even:
    print(", ".join([str(x) for x in set_odd.difference(set_even)]))
else:
    print(", ".join([str(x) for x in set_even.symmetric_difference(set_odd)]))

