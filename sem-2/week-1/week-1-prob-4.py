# 25MCD005 SOHAM DAVE - Rectangles Counting
import sys

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1
        if n == 0:
            break
        
        points_by_x = {}
        for _ in range(n):
            x = int(input_data[idx])
            y = int(input_data[idx+1])
            idx += 2
            if x not in points_by_x:
                points_by_x[x] = []
            points_by_x[x].append(y)
        
        y_pair_counts = {}
        for x in points_by_x:
            ys = points_by_x[x]
            if len(ys) == 2:
                y1, y2 = ys[0], ys[1]
                if y1 > y2:
                    y1, y2 = y2, y1
                pair = (y1, y2)
                y_pair_counts[pair] = y_pair_counts.get(pair, 0) + 1
        
        ans = 0
        for count in y_pair_counts.values():
            if count >= 2:
                ans += (count * (count - 1)) // 2
        
        sys.stdout.write(str(ans) + '\n')

if __name__ == "__main__":
    solve()