# 25MCD005 - PROB - C - The Lakes

def solve():
    import sys
    from collections import deque
    input = sys.stdin.readline

    t = int(input())
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    results = []

    for _ in range(t):
        n, m = map(int, input().split())
        grid = [list(map(int, input().split())) for _ in range(n)]

        max_volume = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    volume = grid[i][j]
                    dq = deque()
                    dq.append((i, j))
                    grid[i][j] = 0

                    while dq:
                        x, y = dq.popleft()
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] > 0:
                                volume += grid[nx][ny]
                                grid[nx][ny] = 0
                                dq.append((nx, ny))

                    if volume > max_volume:
                        max_volume = volume

        results.append(max_volume)

    sys.stdout.write("\n".join(map(str, results)))


if __name__ == "__main__":
    solve()