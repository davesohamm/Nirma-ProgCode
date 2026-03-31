#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>

using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<vector<tuple<int, long long, long long>>> adj(n + 1);
    for (int j = 2; j <= n; ++j) {
        int p;
        long long a, b;
        cin >> p >> a >> b;
        adj[p].push_back({j, a, b});
    }
    
    vector<int> ans(n + 1);
    vector<long long> B_prefix;
    B_prefix.push_back(0);

    auto dfs = [&](auto& self, int u, long long current_A_sum) -> void {
        if (u != 1) {
            auto it = upper_bound(B_prefix.begin(), B_prefix.end(), current_A_sum);
            ans[u] = (it - B_prefix.begin()) - 1;
        }
        for (auto& edge : adj[u]) {
            int v = get<0>(edge);
            long long a = get<1>(edge);
            long long b = get<2>(edge);
            
            B_prefix.push_back(B_prefix.back() + b);
            self(self, v, current_A_sum + a);
            B_prefix.pop_back();
        }
    };

    dfs(dfs, 1, 0);
    
    for (int j = 2; j <= n; ++j) {
        cout << ans[j] << (j == n ? "" : " ");
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