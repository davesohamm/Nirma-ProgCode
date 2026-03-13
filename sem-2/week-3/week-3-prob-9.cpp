// 25MCD005 PROBLEM I - THE LUCKY DRAW
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int get_lis(const vector<int>& a) {
    if (a.empty()) return 0;
    vector<int> tails;
    for (int x : a) {
        auto it = lower_bound(tails.begin(), tails.end(), x);
        if (it == tails.end()) {
            tails.push_back(x);
        } else {
            *it = x;
        }
    }
    return tails.size();
}

void solve() {
    int n;
    if (!(cin >> n)) return;
    vector<int> a(n);
    vector<pair<int, int>> sorted_indices(n);
    for(int i=0; i<n; ++i) {
        cin >> a[i];
        sorted_indices[i] = {a[i], i};
    }
    
    sort(sorted_indices.begin(), sorted_indices.end());
    
    int limit = min(n, 100);
    int max_len = 0;
    
    for(int i=0; i<limit; ++i) {
        int start_idx = sorted_indices[i].second;
        vector<int> current_rotation;
        current_rotation.reserve(n);
        for(int j=0; j<n; ++j) {
            current_rotation.push_back(a[(start_idx + j) % n]);
        }
        max_len = max(max_len, get_lis(current_rotation));
    }
    
    cout << max_len << "\n";
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