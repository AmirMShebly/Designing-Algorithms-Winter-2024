# Title: Backpack Packing

Problem Description:

You are going on a hiking trip and have a backpack with limited capacity. You
want to pack the backpack with items to maximize the total value of the items
you bring while ensuring that the total weight does not exceed the capacity of
the backpack.

Each item has a weight and a value, and you know the maximum capacity of
your backpack. Your task is to determine the maximum total value of items you
can pack into your backpack without exceeding its capacity.

To achieve this, you decide to use the Knapsack algorithm to select the optimal
combination of items to pack. Given the weights and values of available items
and the maximum capacity of the backpack, your task is to determine the
maximum total value of items you can pack into the backpack.

Input:

The input consists of three lines:
The first line contains N (1 fi N fi 100), the number of available items. The
second line contains N integers separated by space, representing the weights of
the items. Each weight is a positive integer not exceeding 1000. The third line
contains N integers separated by space, representing the values of the items.
Each value is a positive integer not exceeding 1000. The fourth line contains an
integer C (1 fi C fi 1000), the maximum capacity of the backpack. Output:

Output:

A single integer, the maximum total value of items you can pack into
the backpack without exceeding its capacity.

Example:

Input: 4 2 3 4 5 3 4 5 6 7

Output: 7

Explanation:
You can pack items with weights [2, 3] and values [3, 4] into the
backpack, resulting in a total weight of 5 and a total value of 7.

Constraints:
1 fi weights, values fi 1000 1 fi C fi 1000
1