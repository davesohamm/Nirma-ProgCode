# 25MCD005 SOHAM DAVE WEEK-9 PROBLEM-4 "Vacation"
import sys

def solve():
    try:
        n = int(sys.stdin.readline())
        if n == 0:
            print(0)
            return

        dp_a, dp_b, dp_c = 0, 0, 0

        for _ in range(n):
            line = sys.stdin.readline().split()
            if not line:
                break
            
            a, b, c = int(line[0]), int(line[1]), int(line[2])
            
            new_dp_a = a + max(dp_b, dp_c)
            new_dp_b = b + max(dp_a, dp_c)
            new_dp_c = c + max(dp_a, dp_b)
            
            dp_a, dp_b, dp_c = new_dp_a, new_dp_b, new_dp_c

        print(max(dp_a, dp_b, dp_c))

    except EOFError:
        pass
    except Exception as e:
        pass

if __name__ == "__main__":
    solve()