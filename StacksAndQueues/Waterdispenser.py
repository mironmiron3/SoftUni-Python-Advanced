from collections import deque

names = input().split()
queue = deque(names)
counter = int(input())
while len(queue) > 1:
    for i in range(counter):
        if i == counter - 1:
            print(f"Removed {queue.popleft()}")
        else:
            queue.append(queue.popleft())
print(f"Last is {deque}")
