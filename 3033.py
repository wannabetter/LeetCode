from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        for j in range(m):
            maxi = -1
            for i in range(n):
                maxi = max(maxi, matrix[i][j])

            for i in range(n):
                matrix[i][j] = maxi if matrix[i][j] == -1 else matrix[i][j]

        return matrix