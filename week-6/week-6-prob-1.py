# 25MCD005 SOHAM DAVE WEEK-6 PROBLEM-1 "Static Range Sum Queries"
import sys

def main():
    input = sys.stdin.readline
    output = sys.stdout.write

    n, q = map(int, input().split())
    x = list(map(int, input().split()))

    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + x[i]

    results = []
    for _ in range(q):
        a, b = map(int, input().split())
        results.append(str(prefix_sum[b] - prefix_sum[a-1]))

    output('\n'.join(results) + '\n')

if __name__ == "__main__":
    main()
