#include <iostream>
#include <vector>

using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<long long> a(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];

    long long count = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = a[i] - (i % a[i]); j <= n; j += a[i]) {
            if (j <= i) continue;
            if (a[i] * a[j] == (long long)i + j) {
                count++;
            }
        }
    }
    cout << count << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}