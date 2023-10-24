from linear_search import verify, numbers

def binary_search(l, target):
    first = 0
    last = len(l) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if l[midpoint] == target:
            return midpoint

        elif l[midpoint] < target:
            first = midpoint + 1

        else:
            last = midpoint - 1

    return None

if __name__ == "__main__":
    result = binary_search(numbers, 12)
    verify(result)

    result = binary_search(numbers, 6)
    verify(result)
