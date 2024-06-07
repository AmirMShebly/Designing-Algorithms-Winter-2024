# Title: Maximizing Profit by Scheduling Tasks

Your task consists of maximizing profits by scheduling tasks.
Consider a scenario where several tasks are available, each with a start time, end time, and profit.
Scheduling should be done in such a way that the total profit obtained is maximized, so that no two selected tasks overlap in their execution time.

Input:

The number of tasks, denoted by N. Each task i(1<= i <= N), includes the following:
- start time
- End time
- Profit


Output:

- The maximum total profit that can be obtained by selecting a subset of tasks such that no two selected tasks overlap in their execution time.
- Selected tasks


Example:


Input:
tasks = [('a', 1, 2, 50), ('b', 3, 5, 20), ('c', 6, 19, 100), ('d', 2, 100, 200), ('e', 0, 1, 100), ('f', 100, 101, 200)]

Output:
Selected Jobs: ['e', 'a', 'd', 'f']
Total Profit: 550


Approach:
Use dynamic programming method to solve this problem.
