#include <bits/stdc++.h>

using namespace std;

int main() {
    // 締め切りが早い順に片付ける以外の方法はない
    int N;
    cin >> N;

    int timeSpent = 0;
    string ans = "Yes";
    vector<pair<int,int>> jobs; // deadlineでソートするため(deadline, timeframe)

    for (int i = 0; i < N; ++i) {
        int A, B; // timeframe, deadline
        cin >> A >> B;
        jobs.emplace_back(B, A);
    }

    sort(jobs.begin(), jobs.end());

    for (auto job : jobs){
        timeSpent += job.second;
        if (timeSpent > job.first){
            ans = "No";
            break;
        }
    }

    cout << ans << endl;
    return 0;
}
