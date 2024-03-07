//
// Created by DELL on 2024/3/7.
//

#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

long run(const vector<int> &vec, int index, int sum, int l, int r) {
    long ans = 0;
    if (sum > r) {
        return 0;
    }
    for (int i = index; i < vec.size(); i++) {
        ans += run(vec, i + 1, sum + vec[i], l, r);
    }
    return (l <= sum && sum <= r) ? ans + 1 : ans;
}

int main() {
    int n, l, r;
    cin >> n >> l >> r;

    vector<int> vec(n);
    for (int i = 0; i < n; i++) {
        cin >> vec[i];
    }

    sort(vec.begin(), vec.end());

    cout << run(vec, 0, 0, l, r);
    return 0;
};