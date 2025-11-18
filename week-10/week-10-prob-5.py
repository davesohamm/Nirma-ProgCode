# 25MCD005 SOHAM DAVE WEEK-10 PROBLEM-5 "Factorial Divisibility"
import sys

n, x = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

counts = [0] * (x + 1)

for val in a:
    if val < x:
        counts[val] += 1

for k in range(1, x):
    counts[k+1] += counts[k] // (k + 1)
    counts[k] = counts[k] % (k + 1)

for k in range(1, x):
    if counts[k] != 0:
        print("No")
        sys.exit()

print("Yes")