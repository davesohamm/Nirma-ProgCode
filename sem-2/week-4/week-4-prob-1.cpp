// 25MCD005 WEEK-4 PROBLEM-A Queue at the School
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n, t;
    if (cin >> n >> t) {
        string s;
        cin >> s;
        while (t--) {
            for (int i = 0; i < n - 1; ++i) {
                if (s[i] == 'B' && s[i + 1] == 'G') {
                    swap(s[i], s[i + 1]);
                    i++;
                }
            }
        }
        cout << s << endl;
    }
    return 0;
}