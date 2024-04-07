# Title: Sorting Employee Salaries
Problem Description:
You are a human resources manager responsible for sorting the salaries of employees in a company. Each employee’s salary is represented
by an integer.

Your task is to implement a function quick_sort_salaries(salaries: List[int]) ->
List[int] that sorts the salaries of employees in ascending order using the Quick
Sort algorithm.

Hint:
The Quick Sort algorithm works as follows:
Choose a pivot element from the list (usually the last element). Partition the
list into two sublists: elements less than the pivot and elements greater than or
equal to the pivot. Recursively apply Quick Sort to the two sublists. Combine
the sorted sublists with the pivot element in between them.
Your function should return the sorted list of employee salaries.

Example:

Input: salaries = [50000, 70000, 40000, 90000, 60000]
Output: [40000, 50000, 60000, 70000, 90000]

Constraints:
1 <= len(salaries) <= 1000 -10^6 <= salaries[i] <= 10^6