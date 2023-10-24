def linear_search(l, target):
    """
    Returns the index position of the target if found, else returns None
    """

    for i, x in enumerate(l):
        if x == target:
            return i
    return None

def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print(f"Target not found in list")


numbers = range(1, 11)

if __name__ == "__main__":
    result = linear_search(numbers, 12)
    verify(result)

    result = linear_search(numbers, 6)
    verify(result)
