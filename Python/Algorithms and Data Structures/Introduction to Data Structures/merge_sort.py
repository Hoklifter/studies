def split(l):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists left and right


    Takes overall O(log n)time
    """

    mid = len(l) // 2

    left = l[:mid]
    right = l[mid:]

    return left, right

def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list

    Runs in overall O(n) time
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l

def merge_sort(l):
    """
    Sorts a list in ascending order

    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublist
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Takes overall O(n log n)time

    """

    if len(l) <= 1:
        return l

    left_half, right_half = split(l)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def verify_sorted(l):
    if len(l) <= 1:
        return True

    return l[0] <= l[1] and verify_sorted(l[1:])


from random import randint
l = []
for _ in range(10):
    l.append(randint(1, 100))


print(f"{l = }")
print(f"After sorting : {merge_sort(l)}")
print(f"Sorting verification in 'l' = {verify_sorted(l)}")
print(f"Sorting verification in sorted 'l' = {verify_sorted(merge_sort(l))}")
