#include <bits/stdc++.h>

typedef long long ll;
using namespace std;
const long long int divisor = 2019; // not prime!!!!

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll L, R;
    cin >> L >> R;
    ll ans = 2020;
    if (R / divisor - L / divisor) { // p≡0 mod 2019なるpをLR間にとれる
        ans = 0;
    } else {
        for (ll i = L; i <= R - 1; ++i) {
            for (ll j = i + 1; j <= R; ++j) {
                long long int residual = i * j % divisor;
                if (!residual) {
                    ans = 0;
                    break;
                }
                ans = min(ans, residual);
            }
        }
    }
    cout << ans << "\n";
    return 0;
}
