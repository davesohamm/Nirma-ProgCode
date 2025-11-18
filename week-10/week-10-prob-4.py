# 25MCD005 SOHAM DAVE WEEK-10 PROBLEM-4 "Finding Borders"
s = input()
n = len(s)

lps = [0] * n
length = 0
i = 1

while i < n:
    if s[i] == s[length]:
        length += 1
        lps[i] = length
        i += 1
    else:
        if length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

borders = []
k = lps[n - 1]

while k > 0:
    borders.append(k)
    k = lps[k - 1]

borders.reverse()
print(*borders)