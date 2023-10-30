
def recursive_binary_search(l, target):
    if len(l) == 0:
        return False

    midpoint = (len(l)) // 2

    if l[midpoint] == target:
        return True
    if l[midpoint] < target:
        return recursive_binary_search(l[midpoint + 1:], target)
    else:
        return recursive_binary_search(l[:midpoint], target)

numbers = range(9)

result = recursive_binary_search(numbers, 12)
print(f"Target found: {result}")


result = recursive_binary_search(numbers, 6)
print(f"Target found: {result}")
