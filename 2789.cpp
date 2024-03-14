//
// Created by DELL on 2024/3/14.
//

#include <vector>

using namespace std;

class Solution {
public:
    long long maxArrayValue(vector<int> &nums) {
        long long index = nums.size() - 1, ans = 0;
        while (index >= 0) {
            long long temp = nums[index];
            for (index; index > 0 && nums[index - 1] <= temp; index--) {
                temp += nums[index - 1];
            }
            ans = ans < temp ? temp : ans;
            index--;
        }
        return ans;
    }
};