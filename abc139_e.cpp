#include <bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    vector<deque<int>> A(N, deque<int>());
    deque<int> matchAvailablePlayers;
    vector<int> daysPassedWhenPlayedMostRecentMatch(N, 0);
    vector<int> desiredOpponentIdx(N, -1);

    for (int i = 0; i < N; ++i) {
        matchAvailablePlayers.emplace_back(i);
        for (int j = 0; j < N - 1; ++j) {
            int a;
            cin >> a;
            A[i].emplace_back(a-1);
        }
    }

    while (!matchAvailablePlayers.empty()){
        int playerIdx = matchAvailablePlayers.front(); matchAvailablePlayers.pop_front();
        auto& matchesOrderForThisPlayer = A[playerIdx];

        if (matchesOrderForThisPlayer.empty()) continue;

        int opponentIdx = matchesOrderForThisPlayer.front(); matchesOrderForThisPlayer.pop_front();

        if (desiredOpponentIdx[opponentIdx] == playerIdx){
            daysPassedWhenPlayedMostRecentMatch[playerIdx] = daysPassedWhenPlayedMostRecentMatch[opponentIdx] = max(daysPassedWhenPlayedMostRecentMatch[playerIdx], daysPassedWhenPlayedMostRecentMatch[opponentIdx]) + 1;
            matchAvailablePlayers.emplace_back(playerIdx);
            matchAvailablePlayers.emplace_back(opponentIdx);
        }else{
            desiredOpponentIdx[playerIdx] = opponentIdx;
        }
    }

    for (auto a : A){
        if (!a.empty()){
            cout << -1;
            return 0;
        }
    }
    cout << *max_element(daysPassedWhenPlayedMostRecentMatch.begin(), daysPassedWhenPlayedMostRecentMatch.end());

    return 0;
}
