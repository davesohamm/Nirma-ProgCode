#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 200005;
vector<pair<int, int>> adj[MAXN];
int dp[MAXN];
int id[MAXN];

void dfs(int u, int p) {
    for (auto edge : adj[u]) {
        int v = edge.first;
        int idx = edge.second;
        if (v != p) {
            // If the edge index is less than the edge that discovered 'u', 
            // we need an extra pass.
            dp[v] = dp[u] + (idx < id[u] ? 1 : 0);
            id[v] = idx;
            dfs(v, u);
        }
    }
}

void solve() {
    int n;
    cin >> n;
    
    for (int i = 1; i <= n; i++) {
        adj[i].clear();
    }
    
    for (int i = 1; i < n; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back({v, i});
        adj[v].push_back({u, i});
    }
    
    dp[1] = 1; // Root takes 1 reading
    id[1] = 0; // Dummy edge index
    dfs(1, 0);
    
    int ans = 0;
    for (int i = 1; i <= n; i++) {
        ans = max(ans, dp[i]);
    }
    
    cout << ans << "\n";
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