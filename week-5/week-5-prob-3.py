# 25MCD005 SOHAM DAVE WEEK-5 PROBLEM-3 "Double Strings"
t = int(input())
for _ in range(t):
    n = int(input())
    words = [input() for _ in range(n)]
    s = set(words)
    ans = ''
    for w in words:
        f = 0
        for i in range(1, len(w)):
            if w[:i] in s and w[i:] in s:
                f = 1
                break
        ans += str(f)
    print(ans)
