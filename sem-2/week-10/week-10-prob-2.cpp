#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int gcd(int a, int b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    vector<int> sorted_a;
    for (int i = 0; i < n; i++) cin >> a[i];

    for (int x : a) {
        if (x % 2 == 0) sorted_a.push_back(x);
    }
    for (int x : a) {
        if (x % 2 != 0) sorted_a.push_back(x);
    }

    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (gcd(sorted_a[i], 2 * sorted_a[j]) > 1) {
                ans++;
            }
        }
    }
    cout << ans << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}