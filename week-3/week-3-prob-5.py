# 25MCD005 SOHAM DAVE WEEK-3 PROBLEM-5 "Fair Numbers"
import sys
def is_fair(n):
    temp = n
    while temp > 0:
        digit = temp % 10
        if digit != 0 and n % digit != 0:
            return False
        temp //= 10
    return True

def solve():
    n = int(sys.stdin.readline())
    while True:
        if is_fair(n):
            print(n)
            return
        n += 1

try:
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()
except (IOError, ValueError):
    pass