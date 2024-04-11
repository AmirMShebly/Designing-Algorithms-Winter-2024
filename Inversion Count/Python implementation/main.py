
def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_count_left = merge_sort(arr[:mid])
    right, inv_count_right = merge_sort(arr[mid:])
    merged, inv_count = merge(left, right)

    return merged, inv_count + inv_count_left + inv_count_right


def merge(left, right):
    merged = []
    inv_count = 0
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inv_count += len(left) - i

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inv_count


def inversion_count(arr):
    _, inv_count = merge_sort(arr)
    return inv_count


def main():
    arr = [1, 20, 6, 4, 5]
    print("Inversion count:", inversion_count(arr))


if __name__ == "__main__":
    main()