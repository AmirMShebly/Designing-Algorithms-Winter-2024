# Title: Plagiarism Detection

Problem Description:

You are developing a plagiarism detection system for a university to identify cases of academic dishonesty. Your task is to compare a student's document with a base
document and determine the degree of similarity between them.

To achieve this, you decide to use the Longest Common Subsequence (LCS) algorithm to identify common sequences of words between the two documents.

Given a base document and a student's document, both represented as strings of words, your task is to find the length of the longest common subsequence (LCS) 
algorithm to identify common sequences of words between the two documents.

Given a base document and a student's document, both represented as strings of words, your task is to find the length of the longest common subsequence (LCS) between them. This will help determine the extent of similarity between the documents.

Input:

The input consists of two parts:

The path to a text file containing the base document.
The path to a text file containing the student's document.
Each text file contains a single string representing the document. The strings consist of English words separated by a space. The length of each string is at most 1000 characters.

Output:

Output two integer, the length of the longest common subsequence of the base document and the student's document and the similarity percentage.

Example:

Input:
base_document.txt
student_document.txt

Output:
LCS length: 87
Similarity Percentage: 47.06%


Explanation:
The longest common subsequence between the base document and the student's document has a length of 87.
