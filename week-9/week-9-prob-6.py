# 25MCD005 SOHAM DAVE WEEK-9 PROBLEM-6 "Removing Digits"
n = int(input())

dp = [float('inf')] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    s = str(i)
    for digit_char in s:
        digit = int(digit_char)
        if digit != 0:
            dp[i] = min(dp[i], 1 + dp[i - digit])

print(dp[n])