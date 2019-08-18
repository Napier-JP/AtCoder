#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N, Q;
    cin >> N >> Q;
    vector<int> parent(N + 1);
    parent.at(1) = 1;

    vector<int> ans(N + 1);
    for (int i = 0; i < N - 1; ++i) {
        int a, b;
        cin >> a >> b;
        parent.at(b) = a;
    }

    for (int i = 0; i < Q; ++i) {
        int p, x;
        cin >> p >> x;
        ans.at(p) += x;
    }

    for (int i = 2; i <= N; ++i) {
        ans.at(i) += ans.at(parent.at(i));
    }

    for (int i = 1; i <= N - 1; ++i) {
        cout << ans.at(i) << " ";
    }
    cout << ans.at(N) << "\n";
    return 0;
}
