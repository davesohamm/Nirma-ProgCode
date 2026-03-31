#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> p(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> p[i];
    }
    
    int max_depth = 0;
    for (int i = 1; i <= n; i++) {
        int depth = 0;
        int curr = i;
        // Traverse up the hierarchy until reaching a root (-1)
        while (curr != -1) {
            depth++;
            curr = p[curr];
        }
        max_depth = max(max_depth, depth);
    }
    
    cout << max_depth << "\n";
    
    return 0;
}