
def max_crossing_subarray(arr, low, mid, high):
    left_sum = float('-inf')
    max_left = mid
    temp_sum = 0

    for i in range(mid, low - 1, -1):
        temp_sum += arr[i]
        if temp_sum > left_sum:
            left_sum = temp_sum
            max_left = i

    right_sum = float('-inf')
    max_right = mid + 1
    temp_sum = 0

    for i in range(mid + 1, high + 1):
        temp_sum += arr[i]
        if temp_sum > right_sum:
            right_sum = temp_sum
            max_right = i

    return max_left, max_right, left_sum + right_sum


def max_subarray(arr, low, high):
    if low == high:
        return low, high, arr[low]

    mid = (low + high) // 2

    left_low, left_high, left_sum = max_subarray(arr, low, mid)
    right_low, right_high, right_sum = max_subarray(arr, mid + 1, high)
    cross_low, cross_high, cross_sum = max_crossing_subarray(arr, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


def max_subarray_divide_and_conquer(arr):
    low, high, max_sum = max_subarray(arr, 0, len(arr) - 1)
    return max_sum, arr[low:high + 1]


def main():
    arr = [7, -2, 4, -1, 9, -6, 5, 4]
    max_sum, max_subarray = max_subarray_divide_and_conquer(arr)
    print("Maximum sum of a contiguous subarray:", max_sum)
    print("The subarray with the maximum sum:", max_subarray)


if __name__ == "__main__":
    main()

