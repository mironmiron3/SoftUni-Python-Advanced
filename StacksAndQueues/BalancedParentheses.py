from collections import deque
is_balanced = True
string = input()
stack_of_opening = []
stack_of_closing = deque()
for item in string:
    if item in ["{","(","["]:
        stack_of_opening.append(item)
    else:
        stack_of_closing.append(item)
if len(stack_of_closing) == len(stack_of_opening):
    while stack_of_closing:
        closing_one = stack_of_closing.popleft()
        opening_one = stack_of_opening.pop()
        if closing_one == ")" and opening_one != "(":
            is_balanced = False
        elif closing_one == "]" and opening_one != "[":
            is_balanced = False
        elif closing_one == "}" and opening_one != "{":
            is_balanced = False
else:
    is_balanced = False
if is_balanced:
    print("YES")
else:
    print("NO")

