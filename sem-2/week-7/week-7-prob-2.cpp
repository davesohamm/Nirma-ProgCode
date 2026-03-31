#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> p(n + 1);
    vector<int> out_degree(n + 1, 0);
    
    for (int i = 2; i <= n; i++) {
        cin >> p[i];
        out_degree[p[i]]++; // Increment child count for the parent
    }
    
    vector<int> leaf_children(n + 1, 0);
    for (int i = 2; i <= n; i++) {
        // If node i has no children, it's a leaf.
        if (out_degree[i] == 0) {
            leaf_children[p[i]]++; // Give its parent a point
        }
    }
    
    bool is_spruce = true;
    for (int i = 1; i <= n; i++) {
        // If it's a non-leaf vertex and has less than 3 leaf children
        if (out_degree[i] > 0 && leaf_children[i] < 3) {
            is_spruce = false;
            break;
        }
    }
    
    cout << (is_spruce ? "Yes" : "No") << "\n";
    
    return 0;
}