count = int(input())
nums = []
for i in range(count):
    data = input()
    if data.startswith("1"):
        nums.append(int(data.split()[1]))
    elif data.startswith("2"):
        if nums:
            nums.pop()
    elif data.startswith("3"):
        print(max(nums))
    elif data.startswith("4"):
        print(min(nums))

while len(nums) > 1:
    print(nums.pop(), end=", ")
print(nums[0])



