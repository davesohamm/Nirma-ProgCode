// 25MCD005 WEEK-4 PROBLEM-D Construct the String
#include <iostream>
#include <string>

using namespace std;

int main() {
    int t;
    if (cin >> t) {
        while (t--) {
            int n, a, b;
            cin >> n >> a >> b;
            string s = "";
            for (int i = 0; i < n; i++) {
                s += (char)('a' + (i % b));
            }
            cout << s << endl;
        }
    }
    return 0;
}