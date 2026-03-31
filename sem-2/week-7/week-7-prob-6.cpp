#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> deg(n + 1, 0);
    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        cin >> u >> v;
        deg[u]++;
        deg[v]++;
    }
    
    int deg3 = 0;
    int center = -1;
    vector<int> leaves;
    
    for (int i = 1; i <= n; ++i) {
        if (deg[i] >= 3) {
            deg3++;
            center = i;
        } else if (deg[i] == 1) {
            leaves.push_back(i);
        }
    }
    
    if (deg3 > 1) {
        cout << "No\n";
    } else {
        cout << "Yes\n";
        if (deg3 == 0) {
            center = leaves[0];
        }
        
        int paths = 0;
        for (int leaf : leaves) {
            if (leaf != center) paths++;
        }
        
        cout << paths << "\n";
        for (int leaf : leaves) {
            if (leaf != center) {
                cout << center << " " << leaf << "\n";
            }
        }
    }
    return 0;
}