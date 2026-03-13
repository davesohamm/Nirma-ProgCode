# 25MCD005 SOHAM DAVE WEEK-6 PROBLEM-7 "Dynamic Range Minimum Queries"
import sys

def main():
    input = sys.stdin.readline
    output = sys.stdout.write
    
    n, q = map(int, input().split())
    x = list(map(int, input().split()))
    
    tree = [float('inf')] * (2 * n)
    tree[n:n + n] = x
    
    for i in range(n - 1, 0, -1):
        tree[i] = min(tree[i * 2], tree[i * 2 + 1])

    def update(index, value):
        index += n
        tree[index] = value
        while index > 1:
            tree[index // 2] = min(tree[index], tree[index ^ 1])
            index //= 2

    def query(left, right):
        res = float('inf')
        left += n
        right += n
        while left < right:
            if left & 1:
                res = min(res, tree[left])
                left += 1
            if right & 1:
                right -= 1
                res = min(res, tree[right])
            left //= 2
            right //= 2
        return res

    results = []
    for _ in range(q):
        line = list(map(int, input().split()))
        
        if line[0] == 1:
            k, u = line[1], line[2]
            update(k - 1, u)
        else:
            a, b = line[1], line[2]
            ans = query(a - 1, b)
            results.append(str(ans))

    output('\n'.join(results) + '\n')

if __name__ == "__main__":
    main()

