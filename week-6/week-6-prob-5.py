# 25MCD005 SOHAM DAVE WEEK-6 PROBLEM-5 "Dynamic Range Sum Queries"
import sys

def main():
    input = sys.stdin.readline
    output = sys.stdout.write

    n, q = map(int, input().split())
    x = list(map(int, input().split()))
    
    bit = [0] * (n + 1)

    def bit_update(index, delta):
        while index <= n:
            bit[index] += delta
            index += index & (-index)

    def prefix_sum(index):
        s = 0
        while index > 0:
            s += bit[index]
            index -= index & (-index)
        return s

    for i in range(n):
        bit_update(i + 1, x[i])

    results = []
    for _ in range(q):
        query = list(map(int, input().split()))
        
        if query[0] == 1:
            k, u = query[1], query[2]
            delta = u - x[k - 1]
            x[k - 1] = u
            bit_update(k, delta)
        else:
            a, b = query[1], query[2]
            ans = prefix_sum(b) - prefix_sum(a - 1)
            results.append(str(ans))

    output('\n'.join(results) + '\n')

if __name__ == "__main__":
    main()
