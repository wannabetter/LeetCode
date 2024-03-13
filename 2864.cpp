//
// Created by DELL on 2024/3/13.
//

#include <string>

using namespace std;

class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        int n = 0;
        for (auto &ch: s) {
            if (ch == '1') {
                n++;
            } else {
                ch = '1';
            }
        }

        for (int i = s.size() - 2; i >= 0 && s.size() - n > 0; i--, n++) {
            s[i] = '0';
        }
        return s;
    }
};