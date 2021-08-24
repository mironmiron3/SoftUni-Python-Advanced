from collections import deque

pizzas = deque(input().split(", "))
employees = input().split(", ")

all_pizzas_made = 0

while pizzas:
    if not employees:
        print(f"Not all orders are completed.\nOrders left {pizzas}")
        break
    current_pizza_order = int(pizzas.popleft())
    if current_pizza_order > 10:
        continue
    current_worker_capacity = int(employees.pop())

    if current_pizza_order <= current_worker_capacity:
        all_pizzas_made += current_pizza_order
        continue
    while current_pizza_order > 0:
        if not employees:
            print(f"Not all orders are completed.\nOrders left {pizzas}")
            break
        #addition = current_pizza_order - current_worker_capacity
        current_pizza_order -= current_worker_capacity
        current_worker_capacity = int(employees.pop())

print(employees)
