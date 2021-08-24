n = int(input())
longest_intersection = []

for _ in range(n):
     first_info, second_info = input().split("-")
     first_start, first_end = first_info.split(",")
     second_start, second_end = second_info.split(",")
     set1 = set()
     set2 = set()
     for i in range(int(first_start),int(first_end)+1):
         set1.add(i)
     for m in range(int(second_start),int(second_end)+1):
         set2.add(m)
     intersection = set1.intersection(set2)
     if len(intersection) > len(longest_intersection):
         longest_intersection = set(intersection)
print(f"Longest intersection is {[i for i in longest_intersection]} with length {len(longest_intersection)}")
set3 = {3, 4, 5}
set4 = [4, 100]
print(set3.intersection(set4))
