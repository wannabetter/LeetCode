//
// Created by DELL on 2024/3/5.
//

#include<cstdio>


const int fx[] = {0, -2, -1, 1, 2, 2, 1, -1, -2};
const int fy[] = {0, 1, 2, 2, 1, -1, -2, -2, -1};

long long dp[40][40];
bool s[40][40];

int Bx, By, Hx, Hy;

int main() {

    scanf("%d%d%d%d", &Bx, &By, &Hx, &Hy);
    Bx += 2, By += 2, Hx += 2, Hy += 2;

    dp[2][1] = 1;
    s[Hx][Hy] = 1;
    for (int i = 1; i <= 8; i++) s[Hx + fx[i]][Hy + fy[i]] = 1;
    for (int i = 2; i <= Bx; i++) {
        for (int j = 2; j <= By; j++) {
            if (s[i][j]) {
                continue;
            }
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
        }
    }
    printf("%lld", dp[Bx][By]);
    return 0;
}