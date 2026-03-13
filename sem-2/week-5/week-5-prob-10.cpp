// 25MCD005 WEEK-5 PROBLEM-J 388535 (Hard Version)
#include <iostream>
#include <vector>

using namespace std;

const int MAX_NODES = 4000000;
int trie[MAX_NODES][2];
int nodes_count = 1;

void insert(int val) {
    int u = 0;
    for (int i = 16; i >= 0; --i) {
        int bit = (val >> i) & 1;
        if (!trie[u][bit]) {
            trie[u][bit] = nodes_count++;
        }
        u = trie[u][bit];
    }
}

int get_min(int x) {
    int u = 0;
    int min_val = 0;
    for (int i = 16; i >= 0; --i) {
        int bit = (x >> i) & 1;
        if (trie[u][bit]) {
            u = trie[u][bit];
        } else {
            u = trie[u][1 - bit];
            min_val |= (1 << i);
        }
    }
    return min_val;
}

int get_max(int x) {
    int u = 0;
    int max_val = 0;
    for (int i = 16; i >= 0; --i) {
        int bit = (x >> i) & 1;
        if (trie[u][1 - bit]) {
            u = trie[u][1 - bit];
            max_val |= (1 << i);
        } else {
            u = trie[u][bit];
        }
    }
    return max_val;
}

void solve() {
    int l, r;
    cin >> l >> r;
    int n = r - l + 1;
    vector<int> a(n);
    
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
        insert(a[i]);
    }

    int ans = 0;
    for (int i = 0; i < n; ++i) {
        int candidate = a[i] ^ l;
        if (get_min(candidate) == l && get_max(candidate) == r) {
            ans = candidate;
            break;
        }
    }
    cout << ans << "\n";

    for(int i = 0; i < nodes_count; ++i) {
        trie[i][0] = 0;
        trie[i][1] = 0;
    }
    nodes_count = 1;
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