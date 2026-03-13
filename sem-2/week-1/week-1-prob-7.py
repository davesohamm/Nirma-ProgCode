# 25MCD005 SOHAM DAVE - Heidi and the Turing Test (Easy)
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
    
    points = []
    num_points = 4 * n + 1
    
    for _ in range(num_points):
        x = int(next(iterator))
        y = int(next(iterator))
        points.append((x, y))

    for i in range(num_points):
        current_points = points[:i] + points[i+1:]
        
        xs = [p[0] for p in current_points]
        ys = [p[1] for p in current_points]
        
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        
        if (max_x - min_x) != (max_y - min_y):
            continue
            
        is_valid = True
        for px, py in current_points:
            on_vertical = (px == min_x or px == max_x) and (min_y <= py <= max_y)
            on_horizontal = (py == min_y or py == max_y) and (min_x <= px <= max_x)
            
            if not (on_vertical or on_horizontal):
                is_valid = False
                break
        
        if is_valid:
            print(points[i][0], points[i][1])
            return

if __name__ == '__main__':
    solve()