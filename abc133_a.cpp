#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N, A, B;
    cin >> N >> A >> B;

    cout << min(A * N, B);
    return 0;
}
