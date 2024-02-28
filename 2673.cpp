//
// Created by DELL on 2024/2/28.
//

#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int minIncrements(int n, vector<int> &cost) {
        int ans = 0;
        for (int i = n - 2; i > 0; i -= 2) {
            ans += abs(cost[i] - cost[i + 1]);
            cost[i / 2] += max(cost[i], cost[i + 1]);
        }
        return ans;
    }
};

