// 25MCD005 PROBLEM A - LLPS
#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    cin >> s;
    char mx = 'a';
    for (char c : s) {
        if (c > mx) mx = c;
    }
    for (char c : s) {
        if (c == mx) cout << c;
    }
    return 0;
}