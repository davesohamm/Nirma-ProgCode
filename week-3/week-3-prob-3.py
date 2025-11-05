# 25MCD005 SOHAM DAVE WEEK-3 PROBLEM-3 "Board Moves"
def main():
    import sys
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        res = 0
        layer = 1
        step = 1
        while layer * 2 < n:
            res += 8 * layer * layer
            layer += 1
        print(res)

if __name__ == "__main__":
    main()
