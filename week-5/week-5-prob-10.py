# 25MCD005 SOHAM DAVE WEEK-5 PROBLEM-10 "Password"
def password(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    length = pi[-1]
    if length == 0:
        print("Just a legend")
        return
    if length in pi[:-1]:
        print(s[:length])
        return
    length = pi[length - 1]
    if length > 0:
        print(s[:length])
    else:
        print("Just a legend")

s = input().strip()
password(s)
