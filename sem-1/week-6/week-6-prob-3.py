# 25MCD005 SOHAM DAVE WEEK-6 PROBLEM-3 "Range Count Query"
import sys
from collections import defaultdict
from bisect import bisect_left, bisect_right

def main():
    input = sys.stdin.readline
    output = sys.stdout.write

    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())

    indices = defaultdict(list)
    for i, val in enumerate(a):
        indices[val].append(i)

    results = []
    for _ in range(q):
        l, r, x = map(int, input().split())
        
        target_list = indices[x]
        
        start = bisect_left(target_list, l - 1)
        end = bisect_right(target_list, r - 1)
        
        results.append(str(end - start))

    output('\n'.join(results) + '\n')

if __name__ == "__main__":
    main()
