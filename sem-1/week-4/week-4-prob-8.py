# 25MCD005 SOHAM DAVE WEEK-4 PROBLEM-8 "Counting Kangaroos is Fun"
n = int(input())
sizes = sorted([int(input()) for _ in range(n)])
left = 0
right = n // 2
hidden = 0
while left < n // 2 and right < n:
    if sizes[right] >= 2 * sizes[left]:
        hidden += 1
        left += 1
        right += 1
    else:
        right += 1
print(n - hidden)
