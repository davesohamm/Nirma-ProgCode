// 25MCD005 PROBLEM H - MINIMIZE THE INTEGER
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void solve() {
    string s;
    cin >> s;
    string even = "", odd = "";
    for (char c : s) {
        if ((c - '0') % 2 == 0) even += c;
        else odd += c;
    }
    
    string res = "";
    int i = 0, j = 0;
    while (i < even.size() && j < odd.size()) {
        if (even[i] < odd[j]) {
            res += even[i++];
        } else {
            res += odd[j++];
        }
    }
    while (i < even.size()) res += even[i++];
    while (j < odd.size()) res += odd[j++];
    
    cout << res << "\n";
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