#   25MCD005 PROBLEM H - Productive Meeting

from sys import stdin
inp = stdin.readline

t = int(inp())

for _ in range(t):
    n = int(inp())
    arr = [int(x) for x in inp().split()]

    if max(arr) > sum(arr) // 2:
        tot = sum(arr) - max(arr)
        arr[arr.index(max(arr))] = tot
    else:
        tot = sum(arr) // 2

    print(tot)

    if sum(arr) % 2:
        arr[arr.index(max(arr))] -= 1

    a = []

    for i in range(n):
        for j in range(arr[i]):
            a.append(i + 1)

    b = a[tot:]

    for c, d in zip(a, b):
        print(c, d)