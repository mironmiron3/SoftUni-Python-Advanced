list_of_nums = [int(el) for el in input().split(", ")]
index_searched = int(input())
item_searched = list_of_nums[index_searched]
sum = 0
for i in range(len(list_of_nums)):
    if list_of_nums[i] < item_searched:
       sum += list_of_nums[i]
       list_of_nums[i] = 0
for k in range(index_searched+1):
    sum += list_of_nums[k]
print(sum)