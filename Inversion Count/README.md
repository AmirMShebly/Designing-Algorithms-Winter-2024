# Title: Shipping Container Loading Efficiency

Problem Description:

You are managing a shipping company that transports goods in containers. Each container has limited space, and your goal is to maximize the efficiency of loading goods
into these containers. To achieve this, you want to count the number of "inversions" in the loading order of the goods.

Each item in the shipment has a specific weight and size. An inversion occurs when a heavier and larger item is loaded into the container before a lighter and smaller
item. Inversions decrease the stability and efficiency of loading, potentially leading to damaged goods or wasted space.
Your task is to write a program that counts the number of inversions in the loading order of goods into a container.

Input:

The input consists of two lines. The first line contains an integer N (1 ≤ N ≤ 10^5), the number of items in the shipment. The second line contains N integers separated by space, representing the weights of the items. Each weight is a positive integer.

Output:

Output a single integer, the number of inversions in the loading order of goods into the container.

Example:
5
10 5 8 15 20

Output:
2

Explanation:
In the given shipment, the inversions occur between items 5 (weight 15) and 3 (weight 8), and between items 5 (weight 20) and 4 (weight 15).

