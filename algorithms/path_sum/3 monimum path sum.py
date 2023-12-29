from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        cur=grid[-1]
        m=len(grid)
        n=len(grid[0])
        for i in range(n-2,-1,-1):
            cur[i]+=cur[i+1]
        for i in range(m-2,-1,-1):
            cur[-1]+=grid[i][-1]
            for j in range(n-2,-1,-1):
                cur[j]=grid[i][j]+min(cur[j], cur[j+1])
        return cur[0]