# 25MCD005 SOHAM DAVE WEEK-2 PROBLEM-5 "Maximum Sum"
import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    t = next(it)
    out_lines = []

    for _ in range(t):
        n = next(it); k = next(it)
        a = [next(it) for _ in range(n)]
        a.sort()

        # prefix sums
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i+1] = pref[i] + a[i]
        total = pref[n]

        best_removed = 10**30
        # x = number of "delete two minimums" operations
        for x in range(k + 1):
            two_x = 2 * x
            if two_x > n:
                break
            rem_max_count = k - x  # how many largest elements we delete
            if rem_max_count > n:
                continue
            removed = pref[two_x] + (pref[n] - pref[n - rem_max_count])
            if removed < best_removed:
                best_removed = removed

        out_lines.append(str(total - best_removed))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()

