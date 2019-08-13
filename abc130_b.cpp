#include <iostream>

using namespace std;
int N, X;

int main() {
    cin >> N >> X;
    int L[N];
    for (int i = 0; i < N; ++i) cin >> L[i];

    int ans = 1;
    int distance = 0;
    for (int i = 0; i < N; ++i) {
        distance += L[i];
        if (distance > X) break;
        ans += 1;
    }
    cout << ans << endl;
    return 0;
}
