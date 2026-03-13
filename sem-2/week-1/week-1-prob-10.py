# 25MCD005 SOHAM DAVE - Gourmet Cat
import sys

def solve():
    a, b, c = map(int, sys.stdin.readline().split())

    full_weeks = min(a // 3, b // 2, c // 2)
    a -= full_weeks * 3
    b -= full_weeks * 2
    c -= full_weeks * 2

    # 0: fish, 1: rabbit, 2: chicken
    # Mon, Tue, Wed, Thu, Fri, Sat, Sun
    schedule = [0, 1, 2, 0, 2, 1, 0]
    
    max_extra_days = 0

    for start_day in range(7):
        cur_a, cur_b, cur_c = a, b, c
        cur_day_idx = start_day
        days_count = 0
        
        while True:
            food_type = schedule[cur_day_idx % 7]
            
            if food_type == 0:
                if cur_a > 0:
                    cur_a -= 1
                else:
                    break
            elif food_type == 1:
                if cur_b > 0:
                    cur_b -= 1
                else:
                    break
            else:
                if cur_c > 0:
                    cur_c -= 1
                else:
                    break
            
            days_count += 1
            cur_day_idx += 1
        
        if days_count > max_extra_days:
            max_extra_days = days_count

    print(full_weeks * 7 + max_extra_days)

if __name__ == "__main__":
    solve()