# 25MCD005 SOHAM DAVE WEEK-9 PROBLEM-1 "Frog 1"
import sys

def main():
    n = int(sys.stdin.readline())
    h = list(map(int, sys.stdin.readline().split()))

    dp = [0] * n
    
    if n == 1:
        print(0)
        return

    dp[1] = abs(h[1] - h[0])

    for i in range(2, n):
        cost1 = dp[i-1] + abs(h[i] - h[i-1])
        cost2 = dp[i-2] + abs(h[i] - h[i-2])
        dp[i] = min(cost1, cost2)

    print(dp[n-1])

if __name__ == "__main__":
    main()