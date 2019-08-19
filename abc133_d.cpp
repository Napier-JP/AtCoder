#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

// まず山0の降雨を頑張って求め、あとは山1 = 2* A_0 - 山0 ...
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N;
    cin >> N;
    vector<ll> A(N);
    for (int i = 0; i < N; ++i) {
        ll a;
        cin >> a;
        A.at(i) = a;
    }
    ll mt0 = accumulate(A.begin(), A.end(), 0ll);
    for (int j = 1; j <= N - 2; ++ ++j) {
        mt0 -= 2 * A.at(j);
    }
    // 山0が求まった
    cout << mt0 << " ";
    ll lastMtPrecipi = mt0;
    for (int k = 0; k <= N - 2; ++k) { // 最後 Mt(N-1) = 2*A[N-2]-Mt(N-2)
        ll thisMtPrecipi = 2 * A.at(k) - lastMtPrecipi;
        cout << thisMtPrecipi;
        (k == N - 2) ? cout << "\n" : cout << " ";
        lastMtPrecipi = thisMtPrecipi;
    }
    return 0;
}
