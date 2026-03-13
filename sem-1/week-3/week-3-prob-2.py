# 25MCD005 SOHAM DAVE WEEK-3 PROBLEM-2 "XORinacci"
def main():
    t = int(input())
    for _ in range(t):
        a, b, n = map(int, input().split())
        if n % 3 == 0:
            print(a)
        elif n % 3 == 1:
            print(b)
        else:
            print(a ^ b)

if __name__ == "__main__":
    main()
