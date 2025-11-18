// 25MCD005 SOHAM DAVE WEEK-10 PROBLEM-6 "Company Queries II"
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int n, q;
const int LOG = 19;
vector<vector<int>> adj;
vector<vector<int>> up;
vector<int> depth;

void dfs(int u, int p, int d) {
    depth[u] = d;
    up[u][0] = p;
    for (int i = 1; i < LOG; ++i) {
        up[u][i] = up[up[u][i - 1]][i - 1];
    }
    for (int v : adj[u]) {
        if (v != p) {
            dfs(v, u, d + 1);
        }
    }
}

int get_lca(int a, int b) {
    if (depth[a] < depth[b]) {
        swap(a, b);
    }

    int diff = depth[a] - depth[b];
    for (int i = LOG - 1; i >= 0; --i) {
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

    cin >> n >> q;

    adj.resize(n + 1);
    up.resize(n + 1, vector<int>(LOG));
    depth.resize(n + 1);

    for (int i = 2; i <= n; ++i) {
        int boss;
        cin >> boss;
        adj[boss].push_back(i);
        adj[i].push_back(boss); 
    }

    dfs(1, 0, 0); 
    up[1][0] = 1;
    for(int i = 1; i < LOG; ++i) {
        up[1][i] = 1;
    }
    for (int i = 2; i <= n; ++i) {
        for (int j = 1; j < LOG; ++j) {
            up[i][j] = up[up[i][j - 1]][j - 1];
        }
    }

    for (int i = 0; i < q; ++i) {
        int a, b;
        cin >> a >> b;
        cout << get_lca(a, b) << "\n";
    }

    return 0;
}