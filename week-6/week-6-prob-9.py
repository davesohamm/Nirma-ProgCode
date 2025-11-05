# 25MCD005 SOHAM DAVE WEEK-6 PROBLEM-9 "Xenia and Bit Operations"
import sys

def main():
    input = sys.stdin.readline
    output = sys.stdout.write
    
    n, m = map(int, input().split())
    size = 1 << n
    a = list(map(int, input().split()))
    
    tree = [0] * (2 * size)
    tree[size:size + size] = a
    
    for i in range(size - 1, 0, -1):
        depth_from_root = i.bit_length() - 1
        op_level = n - depth_from_root
        
        if op_level % 2 == 1:
            tree[i] = tree[2 * i] | tree[2 * i + 1]
        else:
            tree[i] = tree[2 * i] ^ tree[2 * i + 1]

    results = []
    for _ in range(m):
        p, b = map(int, input().split())
        index = p - 1 + size
        tree[index] = b
        
        index //= 2
        op_level = 1
        
        while index > 0:
            if op_level % 2 == 1:
                tree[index] = tree[2 * index] | tree[2 * index + 1]
            else:
                tree[index] = tree[2 * index] ^ tree[2 * index + 1]
            
            index //= 2
            op_level += 1
        
        results.append(str(tree[1]))

    output('\n'.join(results) + '\n')

if __name__ == "__main__":
    main()
