# Title: Maximum Subarray

You are given an array of integers representing the daily stock prices of a company. Your task is to find the contiguous subarray within the array that has the largest sum of elements and determine the maximum sum.

Write a function to solve this problem using Kadane's algorithm which follows a dynamic programming approach.

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
