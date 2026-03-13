// 25MCD005 PROBLEM J - KTH MAX SUBARRAY
#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

void solve() {
    int n, m;
    cin >> n >> m;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<int> L(n), R(n);
    stack<int> s;

    for (int i = 0; i < n; ++i) {
        while (!s.empty() && a[s.top()] <= a[i]) s.pop();
        L[i] = s.empty() ? -1 : s.top();
        s.push(i);
    }

    while (!s.empty()) s.pop();

    for (int i = n - 1; i >= 0; --i) {
        while (!s.empty() && a[s.top()] < a[i]) s.pop();
        R[i] = s.empty() ? n : s.top();
        s.push(i);
    }

    vector<pair<long long, long long>> val_counts;
    for (int i = 0; i < n; ++i) {
        long long count = (long long)(i - L[i]) * (R[i] - i);
        val_counts.push_back({a[i], count});
    }

    sort(val_counts.begin(), val_counts.end(), [](const pair<long long, long long>& x, const pair<long long, long long>& y) {
        return x.first > y.first;
    });

    vector<pair<long long, long long>> unique_counts;
    if (!val_counts.empty()) {
        unique_counts.push_back(val_counts[0]);
        for (size_t i = 1; i < val_counts.size(); ++i) {
            if (val_counts[i].first == unique_counts.back().first) {
                unique_counts.back().second += val_counts[i].second;
            } else {
                unique_counts.push_back(val_counts[i]);
            }
        }
    }

    for (size_t i = 1; i < unique_counts.size(); ++i) {
        unique_counts[i].second += unique_counts[i - 1].second;
    }

    for (int i = 0; i < m; ++i) {
        long long p;
        cin >> p;
        auto it = lower_bound(unique_counts.begin(), unique_counts.end(), p, [](const pair<long long, long long>& elem, long long val) {
            return elem.second < val;
        });
        cout << it->first << "\n";
    }
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