from typing import List


# f[n][k]=min(f[n-1][i])+costs[n][k] 表示第n个房子染第k种颜色需要的花费是从之前房子的最小的总和加上染这种颜色的花费
def minCost(costs: List[List[int]]) -> int:
    F = [costs[0]]
    for index, cost in enumerate(costs[1:]):
        Temp = []
        F_Temp = F[index]
        Temp.append(min(F_Temp[1], F_Temp[2]) + cost[0])
        Temp.append(min(F_Temp[0], F_Temp[2]) + cost[1])
        Temp.append(min(F_Temp[1], F_Temp[0]) + cost[2])
        F.append(Temp)
    return min(F[len(costs) - 1][0], F[len(costs) - 1][1], F[len(costs) - 1][2])
