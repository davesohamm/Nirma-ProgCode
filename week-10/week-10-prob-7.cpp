// 25MCD005 SOHAM DAVE WEEK-10 PROBLEM-7 "Parsa's Humongous Tree"
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

long long dp[100005][2];
vector<int> adj[100005];
int limits[100005][2];

void dfs(int u, int p) {
    dp[u][0] = 0;
    dp[u][1] = 0;
    
    for (int v : adj[u]) {
        if (v == p) continue;
        dfs(v, u);
        
        long long lu = limits[u][0];
        long long ru = limits[u][1];
        long long lv = limits[v][0];
        long long rv = limits[v][1];
        
        dp[u][0] += max(abs(lu - lv) + dp[v][0], abs(lu - rv) + dp[v][1]);
        dp[u][1] += max(abs(ru - lv) + dp[v][0], abs(ru - rv) + dp[v][1]);
    }
}

void solve() {
    int n;
    cin >> n;
    
    for (int i = 1; i <= n; ++i) {
        cin >> limits[i][0] >> limits[i][1];
        adj[i].clear();
    }
    
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    
    dfs(1, 0);
    
    cout << max(dp[1][0], dp[1][1]) << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    
    return 0;
}