# 25MCD005 SOHAM DAVE WEEK-5 PROBLEM-5 "String Matching"
def string_matching(text, pattern):
    combined = pattern + '#' + text
    n = len(combined)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and combined[i] != combined[j]:
            j = pi[j - 1]
        if combined[i] == combined[j]:
            j += 1
        pi[i] = j
    count = sum(1 for x in pi if x == len(pattern))
    print(count)

text = input().strip()
pattern = input().strip()
string_matching(text, pattern)

