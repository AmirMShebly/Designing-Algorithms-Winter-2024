def find_max_profit(tasks):
    tasks.sort(key=lambda x: x[2])

    n = len(tasks)
    dp = [0] * n
    selected_jobs = [[] for _ in range(n)]

    dp[0] = tasks[0][3]
    selected_jobs[0] = [tasks[0]]

    for i in range(1, n):
        included_profit = tasks[i][3]
        l = search(tasks, i)
        if l != -1:
            included_profit += dp[l]
        if included_profit > dp[i-1]:
            dp[i] = included_profit
            if l != -1:
                selected_jobs[i] = selected_jobs[l] + [tasks[i]]
            else:
                selected_jobs[i] = [tasks[i]]
        else:
            dp[i] = dp[i-1]
            selected_jobs[i] = selected_jobs[i-1]

    selected_job_seq = selected_jobs[n-1]
    selected_job_names = [job[0] for job in selected_job_seq]
    max_profit = dp[n-1]

    print(selected_job_names)
    print(max_profit)


def search(jobs, index):
    low, high= 0, index-1
    while low <= high:
        mid = (low + high) // 2
        if jobs[mid][2] <= jobs[index][1]:
            if jobs[mid + 1][2] <= jobs[index][1]:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return -1


def main():

    tasks = [('a', 1, 2, 50), ('b', 3, 5, 20), ('c', 6, 19, 100), ('d', 2, 100, 200), ('e', 0, 1, 100),
             ('f', 100, 101, 200)]
    find_max_profit(tasks)


if __name__ == '__main__':
    main()