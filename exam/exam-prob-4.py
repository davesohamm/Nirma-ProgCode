# 25MCD005 EXAM-PROBLEM-4
"""
Problem: Apple Division

There are n apples, each with a known weight. Your task is to divide the apples into
two groups such that the absolute difference between the total weights of the groups
is as small as possible.

Input:
- The first input line contains an integer n: the number of apples.
- The second line contains n integers p1, p2, ..., pn: the weight of each apple.

Output:
- Print one integer: the minimum possible difference between the weights of the two groups.

Constraints:
1 ≤ n ≤ 20
1 ≤ pi ≤ 10^9

Example:
Input:
    5
    3 2 7 4 1
Output:
    1

Explanation:
One optimal division is:
Group 1: weights {2, 3, 4} → total = 9
Group 2: weights {1, 7} → total = 8
Difference = |9 - 8| = 1
"""


import sys

def solve():
    try:
        line1 = sys.stdin.readline()
        if not line1:
            return
        n = int(line1)
        line2 = sys.stdin.readline()
        if not line2:
            return
        p = list(map(int, line2.split()))

        total_sum = sum(p)
        
        possible_sums = {0}
        for weight in p:
            next_sums = set()
            for s in possible_sums:
                next_sums.add(s + weight)
            possible_sums.update(next_sums)

        min_diff = float('inf')
        for s1 in possible_sums:
            s2 = total_sum - s1
            diff = abs(s1 - s2)
            if diff < min_diff:
                min_diff = diff
        
        print(min_diff)
    except EOFError:
        pass
    except ValueError:
        pass
    
if __name__ == "__main__":
    solve()