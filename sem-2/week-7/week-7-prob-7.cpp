#include <iostream>
#include <vector>

using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<int> b(n + 1);
    int root = -1;
    for (int i = 1; i <= n; ++i) {
        cin >> b[i];
        if (b[i] == i) root = i;
    }
    
    vector<int> p(n + 1);
    vector<int> pos(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> p[i];
        pos[p[i]] = i;
    }
    
    // The root must be the first node in the permutation
    if (p[1] != root) {
        cout << -1 << "\n";
        return;
    }
    
    // Check if the relative distance rules hold up
    for (int i = 1; i <= n; ++i) {
        if (i != root && pos[i] < pos[b[i]]) {
            cout << -1 << "\n";
            return;
        }
    }
    
    vector<int> dist(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        dist[p[i]] = i - 1;
    }
    
    vector<int> w(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        if (i != root) {
            w[i] = dist[i] - dist[b[i]];
        }
    }
    
    for (int i = 1; i <= n; ++i) {
        cout << w[i] << (i == n ? "" : " ");
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