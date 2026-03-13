# 25MCD005 - PROB - G - Unforgivable Curse (easy version)


for _ in range(int(input())):
    n, k = map(int, input().split())
    s1 = input(); s2 = input()
    
    if n <= k:
        print("YES" if s1 == s2 else "NO")
    else:
        i = n - k
        print("YES" if (sorted(s1) == sorted(s2) and s1[i:-i] == s2[i:-i]) else "NO")