// Problem - I - Lexical Sign Sequence - 25MCD005 SOHAM DAVE
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

struct Constraint {
    int a, b, c;
    bool operator<(const Constraint& other) const {
        if (b != other.b) return b < other.b;
        return a > other.a;
    }
};

struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}
    void add(int i, int delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }
    int query(int i) {
        int sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
    int query(int l, int r) {
        return query(r) - query(l - 1);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<int> p(n + 1);
    set<int> mutable_set;
    Fenwick fenwick(n);
    vector<int> v(n + 1);

    for (int i = 1; i <= n; ++i) {
        cin >> p[i];
        if (p[i] == 0) {
            v[i] = -1;
            mutable_set.insert(i);
        } else {
            v[i] = p[i];
        }
        fenwick.add(i, v[i]);
    }

    vector<Constraint> constraints(k);
    for (int i = 0; i < k; ++i) {
        cin >> constraints[i].a >> constraints[i].b >> constraints[i].c;
    }

    sort(constraints.begin(), constraints.end());

    for (int i = 0; i < k; ++i) {
        int a = constraints[i].a;
        int b = constraints[i].b;
        int c = constraints[i].c;
        int current_sum = fenwick.query(a, b);
        if (current_sum < c) {
            int diff = c - current_sum;
            int changes_needed = (diff + 1) / 2;
            
            auto it = mutable_set.upper_bound(b);
            vector<int> to_remove;
            while (changes_needed > 0) {
                if (it == mutable_set.begin()) {
                    cout << "Impossible\n";
                    return 0;
                }
                --it;
                if (*it < a) {
                    cout << "Impossible\n";
                    return 0;
                }
                to_remove.push_back(*it);
                changes_needed--;
            }
            
            for (int idx : to_remove) {
                mutable_set.erase(idx);
                v[idx] = 1;
                fenwick.add(idx, 2);
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        cout << v[i] << (i == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}