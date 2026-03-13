# 25MCD005 SOHAM DAVE WEEK-3 PROBLEM-4 "The Wall"
import math
x, y, a, b = map(int, input().split())
l = x * y // math.gcd(x, y)
start = (a + l - 1) // l * l
if start > b:
    print(0)
else:
    print((b - start) // l + 1)
