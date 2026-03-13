# 25MCD005 SOHAM DAVE WEEK-8 PROBLEM-6 "Pairs"
def check_y(y, uncovered_pairs):
    for a, b in uncovered_pairs:
        if a != y and b != y:
            return False
    return True

def check_all(x, all_pairs):
    uncovered = []
    for a, b in all_pairs:
        if a != x and b != x:
            uncovered.append((a, b))
    
    if not uncovered:
        return True

    y1 = uncovered[0][0]
    if check_y(y1, uncovered):
        return True
        
    y2 = uncovered[0][1]
    if check_y(y2, uncovered):
        return True
        
    return False

n, m = map(int, input().split())
all_pairs = []
for _ in range(m):
    all_pairs.append(list(map(int, input().split())))

if check_all(all_pairs[0][0], all_pairs) or check_all(all_pairs[0][1], all_pairs):
    print("YES")
else:
    print("NO")

