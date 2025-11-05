# 25MCD005 SOHAM DAVE WEEK-1 PROBLEM-2 "STICK LENGTHS"
tally = int(input())
bars = list(map(int, input().split()))
bars.sort()
pivot = bars[tally // 2]
expense = sum(abs(b - pivot) for b in bars)
print(expense)
