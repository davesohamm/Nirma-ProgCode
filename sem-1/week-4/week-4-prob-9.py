# 25MCD005 SOHAM DAVE WEEK-4 PROBLEM-9 "Longest Regular Bracket Sequence"
s = input()
n = len(s)
dp = [0] * n
max_len = 0

for i in range(1, n):
    if s[i] == ')':
        if s[i-1] == '(':
            dp[i] = (dp[i-2] if i >= 2 else 0) + 2
        elif i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
            dp[i] = dp[i-1] + 2 + (dp[i - dp[i-1] - 2] if i - dp[i-1] - 2 >= 0 else 0)
        
        if dp[i] > max_len:
            max_len = dp[i]

if max_len == 0:
    print("0 1")
else:
    count = 0
    for length in dp:
        if length == max_len:
            count += 1
    print(f"{max_len} {count}")
