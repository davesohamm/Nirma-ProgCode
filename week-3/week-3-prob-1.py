# 25MCD005 SOHAM DAVE WEEK-3 PROBLEM-1 "Reordering Array and Sum Check"
def main():
    t = int(input().strip())

    for _ in range(t):
        n, m = map(int, input().split())
        arr = list(map(int, input().split()))

        if sum(arr) == m:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
