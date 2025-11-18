# 25MCD005 SOHAM DAVE WEEK-10 PROBLEM-2 "Theatre Square"
import math

n, m, a = map(int, input().split())

print(math.ceil(n / a) * math.ceil(m / a))