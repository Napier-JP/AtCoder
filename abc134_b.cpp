#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N, D;
    cin >> N >> D;
    cout << (int) ceil((double) N / (D * 2 + 1));
    return 0;
}
