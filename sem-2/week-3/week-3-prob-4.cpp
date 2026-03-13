// 25MCD005 PROBLEM D - Creating a Character
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--) {
        long long str, inte, exp;
        cin >> str >> inte >> exp;
        long long diff = inte + exp - str;
        long long min_e = 0;
        if (diff < 0) {
            min_e = 0;
        } else {
            min_e = (diff / 2) + 1;
        }
        long long ans = max(0LL, exp - min_e + 1);
        cout << ans << endl;
    }
    return 0;
}