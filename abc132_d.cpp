#include <bits/stdc++.h>

using namespace std;
const int divisor = 1000000007;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N, K;
    cin >> N >> K;
    long long int combination[2019][2019];
    for (int i = 0; i < N + 1; ++i) {
        for (int j = 0; j < i + 1; ++j) {
            if (j == 0 || j == i) {
                combination[i][j] = 1;
            } else {
                combination[i][j] = (combination[i-1][j-1] + combination[i-1][j]) % divisor;
            }
        }
    }

    for (int i = 1; i < K + 1; ++i) {
        cout << (combination[N-K+1][i] * combination[K - 1][i - 1]) % divisor << "\n";
    }
    return 0;
}
