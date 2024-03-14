# Title: Student Grades Sorting

Problem Description:
You are a teacher tasked with sorting the grades of students in a class using the Insertion Sort algorithm.
Each student's grade is represented by an integer ranging from 0 to 100.

Your task is to implement a function insertion_sort_grades(grades: List[int]) -> Tuple[List[int], int] that returns a tuple containing the sorted grades and the total
number of comparisons made during the sorting process.

Hint:
The Insertion Sort algorithm works as follows:

Start with the second element of the array (index 1), assuming the first element is already sorted.
Iterate through the unsorted portion of the array, comparing each grade with the grades in the sorted portion, and shifting grades to the right until finding the
correct position for insertion. Insert the current grade into its correct position in the sorted portion.
Repeat steps 2-3 until the entire array is sorted.

Your function should return the sorted grades and the total number of comparisons made during the sorting process.

Example:
input:
grades = [85, 92, 78, 90, 65, 88, 70, 95, 83]

output:
sorted_grades   : [65, 70, 78, 83, 85, 88, 90, 92, 95]
comparisons(Shifts)     : 19


Constraints:

1 <= len(grades) <= 1000
0 <= grades[i] <= 100

