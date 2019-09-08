#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    cin >> N;

    vector<int> A(N);
    int highest = 0, highestCount = 0, second = 0;
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
        if (A[i] == highest){
            ++highestCount;
        }else if(A[i] > highest){
            second = highest;
            highest = A[i];
            highestCount = 1;
        }else{
            second = max(second, A[i]);
        }
    }

    for (auto Ai : A) {
        if (highestCount == 1 && Ai == highest) {
            cout << second << "\n";
        } else {
            cout << highest << "\n";
        }
    }
    return 0;
}
