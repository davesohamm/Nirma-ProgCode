# 25MCD005 SOHAM DAVE WEEK-5 PROBLEM-6 "Finding Borders"
s = input()
n = len(s)
pi = [0] * n
for i in range(1, n):
    j = pi[i - 1]
    while j > 0 and s[i] != s[j]:
        j = pi[j - 1]
    if s[i] == s[j]:
        j += 1
    pi[i] = j
res = []
k = pi[-1]
while k:
    res.append(k)
    k = pi[k - 1]
print(*sorted(res))
