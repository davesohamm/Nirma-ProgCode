# 25MCD005 SOHAM DAVE WEEK-3 PROBLEM-8 "Make It Round"
import sys
input = sys.stdin.readline

def count_factor(x, f):
    c = 0
    while x % f == 0:
        x //= f
        c += 1
    return c

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    cnt2 = count_factor(n, 2)
    cnt5 = count_factor(n, 5)
    k = 1
    need2 = max(0, cnt5 - cnt2)
    need5 = max(0, cnt2 - cnt5)
    
    while need2 > 0 and k*2 <= m:
        k *= 2
        need2 -= 1
    while need5 > 0 and k*5 <= m:
        k *= 5
        need5 -= 1

    while k*10 <= m:
        k *= 10

    k *= m // k
    print(n * k)
