# 25MCD005 SOHAM DAVE WEEK-9 PROBLEM-7 "Stones"
def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    dp = [False] * (k + 1)

    for i in range(1, k + 1):
        for move in a:
            if i >= move and not dp[i - move]:
                dp[i] = True
                break

    if dp[k]:
        print("First")
    else:
        print("Second")

solve()