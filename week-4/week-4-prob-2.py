# 25MCD005 SOHAM DAVE WEEK-4 PROBLEM-2 "Marc's Cakewalk"
def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    miles = 0
    for i in range(len(calorie)):
        miles += (2 ** i) * calorie[i]
    return miles

if __name__ == "__main__":
    n = int(input().strip())
    calorie = list(map(int, input().split()))
    print(marcsCakewalk(calorie))
