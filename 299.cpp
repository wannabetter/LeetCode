//
// Created by 11803 on 2024/3/10.
//

#include <map>
#include <set>
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    string getHint(string secret, string guess) {
        int bull = 0, cow = 0;
        map<char, int> sec;
        set<int> arr;
        for (int i = 0; i < secret.length(); i++) {
            if (secret[i] == guess[i]) {
                bull++;
            } else {
                sec[secret[i]]++;
                arr.insert(i);
            }
        }
        for (int i = 0; i < secret.length(); i++) {
            if (sec[guess[i]] && (arr.find(i) != arr.end())) {
                cow++;
                sec[guess[i]]--;
            }
        }
        return to_string(bull) + "A" + to_string(cow) + "B";
    }
};
