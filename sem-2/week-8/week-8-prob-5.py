# 25MCD005 - PROB - E - Madoka and the Elegant Gift

import sys

def solve():
    n, m = map(int, sys.stdin.readline().split())
    grid = []
    for _ in range(n):
        grid.append(sys.stdin.readline().strip())

    is_elegant = True

    for r in range(n - 1):
        for c in range(m - 1):
            count_ones = 0

            if grid[r][c] == '1':
                count_ones += 1
            if grid[r + 1][c] == '1':
                count_ones += 1
            if grid[r][c + 1] == '1':
                count_ones += 1
            if grid[r + 1][c + 1] == '1':
                count_ones += 1

            if count_ones == 3:
                is_elegant = False
                break

        if not is_elegant:
            break

    if is_elegant:
        print("YES")
    else:
        print("NO")


T = int(sys.stdin.readline())
for _ in range(T):
    solve()