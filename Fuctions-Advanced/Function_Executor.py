def func_executor(*args):
    results = []
    for tup in args:
        func = tup[0]
        what_we_get = func(*tup[1])
        print(*tup[1])
        results.append(what_we_get)

    return results

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
