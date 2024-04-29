# Title: Maximum Subarray with Divide and Conquer 

You are given an array of integers representing the daily stock prices of a company. Your task is to find the contiguous subarray within the array that has the largest sum of elements and determine the maximum sum.

Write a function to solve this problem efficiently.
There are some Dynamic Programming algorithms for this problem. Kadane is one of the algorithms that is widely utilized for this purpose.
But we want you to use a divide and conquer approach.
One common algorithm for this approach is based on the "maximum crossing subarray" idea.
1.Divide: Divide the given array into two halves.
2.Conquer: Recursively find the maximum subarray sum in the left half and the right half of the array.
3.Combine: Find the maximum subarray that crosses the midpoint of the array.
The key step is the "combine" step, where we find the maximum subarray sum that crosses the midpoint of the array. This is done by starting from the midpoint and expanding towards both ends, calculating the sum of elements at each step and keeping track of the maximum sum encountered.


Example:

Input:

Array of daily stock prices: [7, -2, 4, -1, 9, -6, 5, 4]
Output:

Maximum sum of a contiguous subarray: 20
The subarray with the maximum sum: [7, -2, 4, -1, 9]


Constraints:

The array can contain both positive and negative integers.
The array may contain duplicates.
The length of the array is at most 10^5
Each element of the array is within the range[-1000, 1000]

