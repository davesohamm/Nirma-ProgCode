# 25MCD004 EXAM-PROBLEM-1 
"""
Problem: Missing Number

You are given all numbers from 1 to n except one. Your task is to find the missing number.

Input:
- The first input line contains an integer n.
- The second line contains n-1 distinct integers, each between 1 and n (inclusive).

Output:
- Print the missing number.

Constraints:
- 2 <= n <= 2 * 10^5

Example:
Input:
    5
    2 3 1 5
Output:
    4
"""

n = int(input())
numbers = list(map(int, input().split()))
expected_sum = (n * (n + 1)) // 2
actual_sum = sum(numbers)
missing_number = expected_sum - actual_sum
print(missing_number)