#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N, D;
    cin >> N >> D;
    vector<vector<int>> points(N, vector<int>(D));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < D; ++j) {
            int X;
            cin >> X;
            points.at(i).at(j) = X;
        }
    }
    int ans = 0;
    for (int k = 0; k <= N - 2; ++k) { // k番目(0 <= k <= N-2)と
        for (int l = k + 1; l <= N - 1; ++l) { // k < l な l番目を比較
            int squared = 0;
            for (int m = 0; m < D; ++m) {
                int dist = points.at(k).at(m) - points.at(l).at(m);
                squared += dist * dist;
            }
            if (sqrt(squared) == (int)sqrt(squared)) ans += 1;
        }
    }
    cout << ans << "\n";
    return 0;
}
