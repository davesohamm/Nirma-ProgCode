# 25MCD005 SOHAM DAVE WEEK-2 PROBLEM-3 "Challenging Valleys"
import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it))
        arr = [int(next(it)) for _ in range(n)]

        cnt_valid = 0
        i = 0
        while i < n:
            # find maximal segment of equal values starting at i
            j = i
            while j + 1 < n and arr[j + 1] == arr[i]:
                j += 1

            left_ok = (i == 0) or (arr[i - 1] > arr[i])
            right_ok = (j == n - 1) or (arr[j] < arr[j + 1])
            if left_ok and right_ok:
                cnt_valid += 1

            i = j + 1

        out_lines.append("YES" if cnt_valid == 1 else "NO")

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()


