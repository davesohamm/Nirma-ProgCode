# 25MCD005 SOHAM DAVE WEEK-9 PROBLEM-10 "Edit Distance"
def solve():
    str1 = input()
    str2 = input()

    n = len(str1)
    m = len(str2)

    if n < m:
        str1, str2 = str2, str1
        n, m = m, n

    dp = list(range(m + 1))

    for i in range(1, n + 1):
        prev_diag = dp[0]
        dp[0] = i
        for j in range(1, m + 1):
            temp = dp[j]
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            dp[j] = min(dp[j] + 1, 
                        dp[j - 1] + 1, 
                        prev_diag + cost)
            prev_diag = temp

    print(dp[m])

solve()