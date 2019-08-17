#include <bits/stdc++.h>

using namespace std;

int main() {
    int N, L;
    cin >> N >> L;
    // from L to L+N-1
    int sum = (2 * L + N - 1) * N / 2;
    int eat = 0;
    if (L >= 0) eat = L;
    if (L + N - 1 <= 0) eat = L + N - 1;

    cout << sum - eat << endl;
    return 0;
}
