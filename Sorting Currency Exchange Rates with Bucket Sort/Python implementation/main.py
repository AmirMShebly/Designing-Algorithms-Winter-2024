
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def bucket_sort_exchange_rates(rates):

    num_buckets = 10

    buckets = [[] for _ in range(num_buckets)]

    for rate in rates:
        bucket_index = min(int(rate * num_buckets), num_buckets - 1)
        buckets[bucket_index].append(rate)

    for bucket in buckets:
        insertion_sort(bucket)

    sorted_rates = []
    for bucket in buckets:
        sorted_rates.extend(bucket)

    return sorted_rates


def main():
    exchange_rates = [1.5, 0.9, 1.2, 1.8, 1.0, 1.3]
    sorted_rates = bucket_sort_exchange_rates(exchange_rates)
    print(sorted_rates)


if __name__ == "__main__":
    main()
