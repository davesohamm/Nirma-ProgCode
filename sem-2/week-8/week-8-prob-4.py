# 25MCD005 - PROB - D - Arrow Path

def solve():
    n = int(input())
    c1 = input()
    c2 = input()

    for i in range(2, n - 1, 2):
        if c2[i] == '<' and (c1[i - 1] == '<' or c1[i + 1] == '<'):
            print("NO")
            return

    print("YES")


for _ in range(int(input())):
    solve()