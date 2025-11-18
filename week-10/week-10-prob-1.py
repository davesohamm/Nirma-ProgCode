# 25MCD005 SOHAM DAVE WEEK-10 PROBLEM-1 "Stick Lengths"
n = int(input())
p = list(map(int, input().split()))

p.sort()

median = p[n // 2]

total_cost = 0
for length in p:
    total_cost += abs(length - median)

print(total_cost)