# 25MCD005 SOHAM DAVE WEEK-8 PROBLEM-1 "New Year Transportation"
n, t = map(int, input().split())
a = list(map(int, input().split()))

current = 1
while current < t:
    current += a[current - 1]

if current == t:
    print("YES")
else:
    print("NO")
