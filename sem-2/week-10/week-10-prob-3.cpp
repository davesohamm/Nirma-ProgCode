#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool is_rbs(string s) {
    int balance = 0;
    for (char c : s) {
        if (c == '(') balance++;
        else balance--;
        if (balance < 0) return false;
    }
    return balance == 0;
}

void solve() {
    string a;
    cin >> a;
    int n = a.length();
    char first = a[0];
    char last = a[n - 1];

    if (first == last) {
        cout << "NO" << endl;
        return;
    }

    char third = ' ';
    for (char c : {'A', 'B', 'C'}) {
        if (c != first && c != last) {
            third = c;
            break;
        }
    }

    char options[] = {'(', ')'};
    for (char t_bracket : options) {
        string b = "";
        for (char c : a) {
            if (c == first) b += '(';
            else if (c == last) b += ')';
            else b += t_bracket;
        }
        if (is_rbs(b)) {
            cout << "YES" << endl;
            return;
        }
    }

    cout << "NO" << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}