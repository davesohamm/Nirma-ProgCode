#include <iostream>
#include <vector>
#include <set>

using namespace std;

struct Edge {
    int to;
    int weight;
};

vector<vector<Edge>> adj;
set<int> reachable_from_a;
bool possible;
int n, a, b;

void dfs_a(int u, int p, int cur_xor) {
    if (u == b) {
        if (cur_xor == 0) possible = true;
        return;
    }
    reachable_from_a.insert(cur_xor);
    for (auto& edge : adj[u]) {
        if (edge.to != p) {
            dfs_a(edge.to, u, cur_xor ^ edge.weight);
        }
    }
}

void dfs_b(int u, int p, int cur_xor) {
    if (u != b && reachable_from_a.count(cur_xor)) {
        possible = true;
    }
    for (auto& edge : adj[u]) {
        if (edge.to != p) {
            if (u == b || edge.to != b) {
                dfs_b(edge.to, u, cur_xor ^ edge.weight);
            }
        }
    }
}

void solve() {
    cin >> n >> a >> b;
    adj.assign(n + 1, vector<Edge>());
    reachable_from_a.clear();
    possible = false;

    for (int i = 0; i < n - 1; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    dfs_a(a, -1, 0);
    if (possible) {
        cout << "YES" << endl;
        return;
    }

    dfs_b(b, -1, 0);
    
    if (possible) cout << "YES" << endl;
    else cout << "NO" << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}