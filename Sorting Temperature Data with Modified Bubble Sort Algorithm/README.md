# Title: Sorting Temperature Data with Bubble Sort


Problem Description:
You are a meteorologist analyzing temperature data collected from various weather stations. Each data point consists of only the temperature recorded (an integer representing the temperature in degrees Celsius).

Your task is to implement a function bubble_sort_temperatures(temperature_data: List[int]) -> List[int] that sorts the temperature data in ascending order using the Bubble Sort algorithm. Additionally, you need to modify the Bubble Sort algorithm so that it stops when the sorting is complete, rather than continuing until the end of the two nested for loops. Print the stage at which the algorithm stopped.

Hint:
The Bubble Sort algorithm works as follows:

Start from the beginning of the list, compare adjacent elements, and swap them if they are in the wrong order (i.e., if the temperature of the current data point is greater than the temperature of the next data point). Repeat this process for each pair of adjacent elements in the list until no swaps are needed, indicating that the list is sorted. Your function should return the sorted list of temperature data.

Example:

Input:
temperature_data = [-7, -12, 24, 15, 3, -1, 14, 6]

Output:
Sorted temperature data: [-12, -7, -1, 3, 6, 14, 15, 24]
Algorithm stopped at stage 12

Constraints:

1 <= len(temperature_data) <= 1000
-100 <= temperature <= 100

Bubble Sort is not very efficient for large datasets but can be useful for sorting small lists or as a teaching tool for understanding sorting algorithms.

