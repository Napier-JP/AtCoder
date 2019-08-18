#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a.at(i);
    }
    int ans = 0;
    for (int j = 0; j < n - 2; ++j) {
        if (a.at(j) < a.at(j + 1) && a.at(j + 1) < a.at(j + 2)) ++ans;
        if (a.at(j) > a.at(j + 1) && a.at(j + 1) > a.at(j + 2)) ++ans;
    }
    cout << ans << endl;
    return 0;
}
