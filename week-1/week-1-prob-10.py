# 25MCD005 SOHAM DAVE WEEK-1 PROBLEM-10 "VOLTAGE KEEPSAKE"
n, p = map(int, input().split())
devices = [tuple(map(int, input().split())) for _ in range(n)]

total_consumption = sum(ai for ai, _ in devices)
if total_consumption <= p:
    print(-1)
else:
    left, right = 0.0, 1e18
    for _ in range(100):
        mid = (left + right) / 2
        extra = sum(max(0.0, ai * mid - bi) for ai, bi in devices)
        if extra <= p * mid:
            left = mid
        else:
            right = mid
    print(f"{left:.10f}")
