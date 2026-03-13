// 25MCD005 WEEK-5 PROBLEM-C Mocha and Red and Blue
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void solve() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    
    int first_fixed = -1;
    for(int i = 0; i < n; ++i) {
        if(s[i] != '?') {
            first_fixed = i;
            break;
        }
    }

    if(first_fixed == -1) {
        s[0] = 'B'; 
        for(int i = 1; i < n; ++i) {
            s[i] = (s[i-1] == 'B' ? 'R' : 'B');
        }
    } else {
        for(int i = first_fixed - 1; i >= 0; --i) {
            s[i] = (s[i+1] == 'B' ? 'R' : 'B');
        }
        for(int i = first_fixed + 1; i < n; ++i) {
            if(s[i] == '?') {
                s[i] = (s[i-1] == 'B' ? 'R' : 'B');
            }
        }
    }
    cout << s << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}