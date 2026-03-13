// 25MCD005 SOHAM DAVE WEEK-7 PROBLEM-8 "Distance Queries"
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

const int MAXN = 200005;
int LOG;
vector<int> adj[MAXN];
int depth[MAXN];
int up[MAXN][20];

void dfs(int u, int p, int d) {
    depth[u] = d;
    up[u][0] = p;
    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u, d + 1);
        }
    }
}

int lca(int a, int b) {
    if (depth[a] < depth[b]) {
        swap(a, b);
    }

    int diff = depth[a] - depth[b];
    for (int i = 0; i < LOG; ++i) {
        if ((diff >> i) & 1) {
            a = up[a][i];
        }
    }

    if (a == b) {
        return a;
    }

    for (int i = LOG - 1; i >= 0; --i) {
        if (up[a][i] != up[b][i]) {
            a = up[a][i];
            b = up[b][i];
        }
    }

    return up[a][0];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, q;
    cin >> n >> q;

    LOG = (int)ceil(log2(n + 1));

    for (int i = 0; i < n - 1; ++i) {
        int a, b;
        cin >> a >> b;
        --a; 
        --b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    dfs(0, 0, 0);

    for (int i = 1; i < LOG; ++i) {
        for (int u = 0; u < n; ++u) {
            up[u][i] = up[up[u][i - 1]][i - 1];
        }
    }

    for (int i = 0; i < q; ++i) {
        int a, b;
        cin >> a >> b;
        --a;
        --b;
        int l = lca(a, b);
        int dist = depth[a] + depth[b] - 2 * depth[l];
        cout << dist << "\n";
    }

    return 0;
}
