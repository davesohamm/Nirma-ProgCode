# 25MCD005 SOHAM DAVE WEEK-10 PROBLEM-3 "Books"
import sys

def solve():
    try:
        n_t = sys.stdin.readline().split()
        if not n_t:
            return 
        n = int(n_t[0])
        t = int(n_t[1])
        
        a = list(map(int, sys.stdin.readline().split()))
        
        if not a:
            print(0)
            return

        left = 0
        current_sum = 0
        max_books = 0
        
        for right in range(n):
            current_sum += a[right]
            
            while current_sum > t:
                current_sum -= a[left]
                left += 1
                
            max_books = max(max_books, right - left + 1)
            
        print(max_books)
        
    except EOFError:
        pass
    except Exception as e:
        pass

if __name__ == "__main__":
    solve()