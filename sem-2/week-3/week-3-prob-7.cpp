// 25MCD005 PROBLEM G - DIVIDE THE STUDENTS
#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

void solve() {
    int a, b, c;
    cin >> a >> b >> c;

    int ans_1_2 = max(a, (c + 1) / 2);
    int ans_2_1 = max((a + 1) / 2, c);
    
    int min_bottleneck = min(ans_1_2, ans_2_1);
    
    int total_avg = (a + b + c + 2) / 3;
    
    cout << max(total_avg, min_bottleneck) << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}