#include <bits/stdc++.h>

using namespace std;

long long int W, H, x, y; // W * H can be 10^18, causing int to overflow

int main() {
    cin >> W >> H >> x >> y;
    cout << fixed << setprecision(10) << (double) W * H / 2 << " ";
    if (x * 2 == W && y * 2 == H) cout << 1 << endl;
    else cout << 0 << endl;
    return 0;
}
