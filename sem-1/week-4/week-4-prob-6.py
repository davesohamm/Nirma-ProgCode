# 25MCD005 SOHAM DAVE WEEK-4 PROBLEM-6 "Schedule Management"
import sys
input = sys.stdin.readline

def can_complete(T, n, m, count):
    total = 0
    for c in count:
        if c >= T:
            total += T
        else:
            total += c + (T - c)//2
        if total >= m:
            return True
    return total >= m

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    tasks = list(map(int, input().split()))
    count = [0] * n
    for a in tasks:
        count[a-1] += 1
    l, r = 0, 2 * m
    while l < r:
        mid = (l + r) // 2
        if can_complete(mid, n, m, count):
            r = mid
        else:
            l = mid + 1
    print(l)

