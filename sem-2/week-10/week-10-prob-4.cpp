#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    int n;
    if (!(cin >> n)) return;

    vector<pair<long long, int>> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i].first;
        a[i].second = i;
    }

    sort(a.begin(), a.end());

    vector<long long> prefix(n);
    prefix[0] = a[0].first;
    for (int i = 1; i < n; i++) {
        prefix[i] = prefix[i - 1] + a[i].first;
    }

    vector<int> res(n);
    int last = 0;
    for (int i = 0; i < n; i++) {
        if (last < i) last = i;
        while (last < n - 1 && prefix[last] >= a[last + 1].first) {
            last++;
        }
        res[a[i].second] = last;
    }

    for (int i = 0; i < n; i++) {
        cout << res[i] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";
}

int main() {
    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        solve();
    }
    return 0;
}