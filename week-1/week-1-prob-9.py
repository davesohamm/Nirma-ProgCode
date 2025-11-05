# 25MCD005 SOHAM DAVE WEEK-1 PROBLEM-9 "VALHALLA SIEGE"
import sys
import bisect
input = sys.stdin.readline

n, q = map(int, input().split())
strengths = list(map(int, input().split()))
arrows = list(map(int, input().split()))

prefix = [0] * n
prefix[0] = strengths[0]
for i in range(1, n):
    prefix[i] = prefix[i-1] + strengths[i]

total_arrows = 0
for k in arrows:
    total_arrows += k
    if total_arrows >= prefix[-1]:
        print(n)
        total_arrows = 0
    else:
        idx = bisect.bisect_right(prefix, total_arrows)
        print(n - idx)
