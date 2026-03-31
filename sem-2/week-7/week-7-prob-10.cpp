#include <iostream>
#include <vector>
#include <queue>

using namespace std;

void solve() {
    int n, k;
    cin >> n >> k;
    vector<int> marked(k);
    for (int i = 0; i < k; ++i) {
        cin >> marked[i];
    }
    
    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    
    if (k <= 1) {
        cout << 0 << "\n";
        return;
    }

    auto bfs = [&](int start, int& farthest) {
        vector<int> dist(n + 1, -1);
        queue<int> q;
        q.push(start);
        dist[start] = 0;
        
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : adj[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.push(v);
                }
            }
        }
        
        int max_d = -1;
        farthest = start;
        for (int m : marked) {
            if (dist[m] > max_d) {
                max_d = dist[m];
                farthest = m;
            }
        }
        return max_d;
    };

    int u, v;
    bfs(marked[0], u);
    int diam = bfs(u, v);
    
    // Middle bounds
    cout << (diam + 1) / 2 << "\n";
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