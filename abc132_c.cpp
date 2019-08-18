#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    vector<int> d(n);
    for (int i = 0; i < n; ++i) {
        cin >> d.at(i);
    }
    sort(d.begin(), d.end());
    cout << d.at(n / 2) - d.at(n / 2 - 1) << "\n";
    return 0;
}
