#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        int n;
        cin >> n;
        int current_sum = 0;
        for (int i = 0; i < n - 1; ++i) {
            int a;
            cin >> a;
            current_sum += a;
        }
        cout << -current_sum << "\n";
    }
    return 0;
}