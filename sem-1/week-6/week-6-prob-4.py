# 25MCD005 SOHAM DAVE WEEK-6 PROBLEM-4 "Static Range Minimum Queries"
import sys
import math

def main():
    input = sys.stdin.readline
    output = sys.stdout.write

    n, q = map(int, input().split())
    x = list(map(int, input().split()))

    if n == 0:
        return

    K = int(math.log2(n)) + 1
    st = [[0] * n for _ in range(K + 1)]
    
    logs = [0] * (n + 1)
    for i in range(2, n + 1):
        logs[i] = logs[i // 2] + 1

    for i in range(n):
        st[0][i] = x[i]

    for k in range(1, K + 1):
        i = 0
        while i + (1 << k) <= n:
            st[k][i] = min(st[k - 1][i], st[k - 1][i + (1 << (k - 1))])
            i += 1

    results = []
    for _ in range(q):
        a, b = map(int, input().split())
        l = a - 1
        r = b - 1
        length = r - l + 1
        k = logs[length]
        ans = min(st[k][l], st[k][r - (1 << k) + 1])
        results.append(str(ans))

    output('\n'.join(results) + '\n')

if __name__ == "__main__":
    main()
