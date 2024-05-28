
def knapsack_max_value(input):
    num_items, capacity = input[0], input[-1]
    weights, values = input[1:num_items+1], input[num_items+1:-1]

    dp = [[0] * (capacity + 1) for _ in range(num_items + 1)]

    for i in range(1, num_items + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
            print(dp[i])

    return dp[num_items][capacity]


def main():
    input = [4, 2, 3, 4, 5, 3, 4, 5, 6, 7]
    print("The maximum value is ", knapsack_max_value(input))


if __name__ == '__main__':
    main()





