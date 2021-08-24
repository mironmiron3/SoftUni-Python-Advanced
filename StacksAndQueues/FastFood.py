from collections import deque
quantity_available = int(input())
orders_left = []
queue = deque(input().split())
list_of_orders = [int(i) for i in queue]
print(max(list_of_orders))


while queue:
    order = int(queue.popleft())
    if order > quantity_available:
        orders_left.append(str(order))
    else:
        quantity_available -= order
if not orders_left:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(orders_left)}")

