
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    int n;
    if (!(cin >> n)) return;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    a.erase(unique(a.begin(), a.end()), a.end());
    
    int new_n = a.size();
    if (new_n == 1) {
        cout << 1 << "\n";
        return;
    }

    int count = 2; 
    for (int i = 1; i < new_n - 1; i++) {
        if ((a[i] > a[i - 1] && a[i] > a[i + 1]) || 
            (a[i] < a[i - 1] && a[i] < a[i + 1])) {
            count++;
        }
    }
    cout << count << "\n";
}

int main() {
    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        solve();
    }
    return 0;
}