# 25MCD005 SOHAM DAVE - Vasya the Architect
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
    except StopIteration:
        return

    bricks = []
    for _ in range(n):
        x1 = int(next(iterator))
        y1 = int(next(iterator))
        x2 = int(next(iterator))
        y2 = int(next(iterator))
        
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        min_y = min(y1, y2)
        max_y = max(y1, y2)
        
        a = abs(x1 - x2)
        w = a ** 3
        
        two_cx = x1 + x2
        two_cy = y1 + y2
        
        bricks.append({
            'min_x': min_x,
            'max_x': max_x,
            'min_y': min_y,
            'max_y': max_y,
            'w': w,
            '2cx': two_cx,
            '2cy': two_cy
        })

    for k in range(1, n + 1):
        for supporter in range(k - 1):
            total_w = 0
            total_2mom_x = 0
            total_2mom_y = 0
            
            for upper in range(supporter + 1, k):
                b = bricks[upper]
                total_w += b['w']
                total_2mom_x += b['w'] * b['2cx']
                total_2mom_y += b['w'] * b['2cy']
            
            supporter_b = bricks[supporter]
            
            lhs_x = 2 * total_w * supporter_b['min_x']
            rhs_x = 2 * total_w * supporter_b['max_x']
            
            if not (lhs_x <= total_2mom_x <= rhs_x):
                print(k - 1)
                return
                
            lhs_y = 2 * total_w * supporter_b['min_y']
            rhs_y = 2 * total_w * supporter_b['max_y']
            
            if not (lhs_y <= total_2mom_y <= rhs_y):
                print(k - 1)
                return

    print(n)

if __name__ == '__main__':
    solve()