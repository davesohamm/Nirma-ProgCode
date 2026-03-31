#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<long long> a(n), b(n), c(n);
    
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) cin >> b[i];
    
    long long max_c = -2e18; // Initialize with a very small number
    for (int i = 0; i < n; i++) {
        c[i] = a[i] - b[i];
        if (c[i] > max_c) {
            max_c = c[i];
        }
    }
    
    vector<int> ans;
    for (int i = 0; i < n; i++) {
        if (c[i] == max_c) {
            ans.push_back(i + 1); // 1-based index
        }
    }
    
    cout << ans.size() << "\n";
    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] << (i + 1 == ans.size() ? "" : " ");
    }
    cout << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}