// 25MCD005 PROBLEM C - PolandBall and Game
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m;
    cin >> n >> m;
    unordered_set<string> pb_words;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        pb_words.insert(s);
    }
    int common = 0;
    for (int i = 0; i < m; i++) {
        string s;
        cin >> s;
        if (pb_words.count(s)) {
            common++;
        }
    }
    if (n > m) {
        cout << "YES" << endl;
    } else if (m > n) {
        cout << "NO" << endl;
    } else {
        if (common % 2 == 1) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
    return 0;
}