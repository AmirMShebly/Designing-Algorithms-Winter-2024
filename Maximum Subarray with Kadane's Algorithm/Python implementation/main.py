def max_subarray_sum(arr):
    max_sum = float('-inf')
    current_sum = 0
    start_index = end_index = 0

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            end_index = i

        if current_sum < 0:
            current_sum = 0
            start_index = i + 1

    if max_sum == float('-inf'):
        max_sum = max(arr)
        start_index = arr.index(max_sum)
        end_index = start_index

    return max_sum, arr[start_index:end_index + 1]


def main():
    arr = [7, -2, 4, -1, 9, -6, 5, 4]
    max_sum, max_subarray = max_subarray_sum(arr)
    print("Maximum sum of a contiguous subarray:", max_sum)
    print("The subarray with the maximum sum:", max_subarray)


if __name__ == "__main__":
    main()
