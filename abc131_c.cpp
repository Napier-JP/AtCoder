#include <bits/stdc++.h>

using namespace std;

template<typename T>
T myGCD(T numA, T numB) {
    if (numA < numB) swap(numA, numB);
    if (numB == 0) return numA;
    numA = numA % numB;
    return myGCD(numB, numA);
};

template<typename T>
T myLCM(T numA, T numB) {
    return numA * numB / myGCD<T>(numA, numB);
}

int main() {
    long long int a, b, c, d;
    cin >> a >> b >> c >> d;
    long long int divC = b / c - (a - 1) / c;
    long long int divD = b / d - (a - 1) / d;
    auto lcmCD = myLCM<long long>(c, d);
    long long int divCD = b / lcmCD - (a - 1) / lcmCD;
    cout << b - a + 1 - divC - divD + divCD << endl;
    return 0;
}
