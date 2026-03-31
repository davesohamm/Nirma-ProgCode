#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const int MAXN = 300005;
const int INF = 1e9;
int l[MAXN], r[MAXN];
string s;

int dfs(int u) {
    if (l[u] == 0 && r[u] == 0) return 0; // Reached a leaf
    
    int ans = INF;
    if (l[u] != 0) {
        ans = min(ans, dfs(l[u]) + (s[u] == 'L' ? 0 : 1));
    }
    if (r[u] != 0) {
        ans = min(ans, dfs(r[u]) + (s[u] == 'R' ? 0 : 1));
    }
    return ans;
}

void solve() {
    int n;
    cin >> n;
    cin >> s;
    s = " " + s; // 1-based indexing for the string
    
    for (int i = 1; i <= n; i++) {
        cin >> l[i] >> r[i];
    }
    
    cout << dfs(1) << "\n";
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