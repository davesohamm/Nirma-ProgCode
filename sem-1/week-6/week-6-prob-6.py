# 25MCD005 SOHAM DAVE WEEK-6 PROBLEM-6 "Range Update Queries"
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

    results = []
    for _ in range(q):
        query = list(map(int, input().split()))
        
        if query[0] == 1:
            a, b, u = query[1], query[2], query[3]
            bit_update(a, u)
            if b + 1 <= n:
                bit_update(b + 1, -u)
        else:
            k = query[1]
            ans = x[k - 1] + prefix_sum(k)
            results.append(str(ans))

    output('\n'.join(results) + '\n')

if __name__ == "__main__":
    main()
