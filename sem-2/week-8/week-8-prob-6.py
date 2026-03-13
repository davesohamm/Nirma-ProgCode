# 25MCD005 - PROB - F - Anonymous Informant

import sys

def solve():
    n, k = map(int, sys.stdin.readline().split())
    b = list(map(int, sys.stdin.readline().split()))

    current_idx = n - 1
    steps_to_simulate = min(k, n)

    for _ in range(steps_to_simulate):
        val = b[current_idx]
        if val > n:
            print("No")
            return

        current_idx = (current_idx - val + n) % n

    print("Yes")


T = int(sys.stdin.readline())
for _ in range(T):
    solve()