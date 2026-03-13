#include <iostream>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    if (m % n != 0) {
        cout << -1 << endl;
        return 0;
    }
    int d = m / n;
    int res = 0;
    while (d % 2 == 0) {
        d /= 2;
        res++;
    }
    while (d % 3 == 0) {
        d /= 3;
        res++;
    }
    if (d != 1) {
        cout << -1 << endl;
    } else {
        cout << res << endl;
    }
    return 0;
}