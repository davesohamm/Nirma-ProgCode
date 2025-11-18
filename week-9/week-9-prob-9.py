# 25MCD005 SOHAM DAVE WEEK-9 PROBLEM-9 "Counting Numbers"
import sys

sys.setrecursionlimit(2000)

def count_dp(s, pos, prev_digit, tight, leading_zeros, dp):
    if pos == len(s):
        return 1
    
    if not tight and dp[pos][prev_digit][int(leading_zeros)] != -1:
        return dp[pos][prev_digit][int(leading_zeros)]
    
    upper_limit = int(s[pos]) if tight else 9
    
    total_count = 0
    
    for current_digit in range(upper_limit + 1):
        if leading_zeros and current_digit == 0:
            new_tight = tight and (current_digit == upper_limit)
            total_count += count_dp(s, pos + 1, 10, new_tight, True, dp)
        else:
            if current_digit != prev_digit:
                new_tight = tight and (current_digit == upper_limit)
                total_count += count_dp(s, pos + 1, current_digit, new_tight, False, dp)
    
    if not tight:
        dp[pos][prev_digit][int(leading_zeros)] = total_count
        
    return total_count

def get_count(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
        
    s = str(n)
    length = len(s)
    dp = [[[-1] * 2 for _ in range(11)] for _ in range(length)]
    
    return count_dp(s, 0, 10, True, True, dp)

a, b = map(int, input().split())
ans_b = get_count(b)
ans_a = get_count(a - 1)
print(ans_b - ans_a)