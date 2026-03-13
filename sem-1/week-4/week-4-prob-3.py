# 25MCD005 SOHAM DAVE WEEK-4 PROBLEM-3 "Luck Balance"
def luckBalance(k, contests):
    important = [l for l, t in contests if t == 1]
    unimportant = [l for l, t in contests if t == 0]
    important.sort(reverse=True)
    total = sum(unimportant)
    total += sum(important[:k])
    total -= sum(important[k:])
    return total

if __name__ == "__main__":
    n, k = map(int, input().split())
    contests = [list(map(int, input().split())) for _ in range(n)]
    print(luckBalance(k, contests))
