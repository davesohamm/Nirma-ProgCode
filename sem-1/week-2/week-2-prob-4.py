# 25MCD005 SOHAM DAVE WEEK-2 PROBLEM-4 "Dora and Search"
import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]

        l, r = 0, n - 1
        mn, mx = 1, n

        while l <= r:
            if a[l] == mn:
                l += 1
                mn += 1
            elif a[l] == mx:
                l += 1
                mx -= 1
            elif a[r] == mn:
                r -= 1
                mn += 1
            elif a[r] == mx:
                r -= 1
                mx -= 1
            else:
                break

        if l <= r:
            out_lines.append(f"{l+1} {r+1}")
        else:
            out_lines.append("-1")

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()

