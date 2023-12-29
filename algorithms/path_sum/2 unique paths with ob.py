# This can be doing using 1D dp too
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0]) 
        dp=[[None for j in range(n)] for i in range(m)]
        dp[-1][-1]=1 if obstacleGrid[-1][-1]==0 else 0
        for i in range(m-2,-1,-1):
            dp[i][-1]=dp[i+1][-1] if obstacleGrid[i][-1]==0 else 0
        for i in range(n-2,-1,-1):
            dp[-1][i]=dp[-1][i+1] if obstacleGrid[-1][i]==0 else 0
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[i][j]=dp[i+1][j]+dp[i][j+1] if obstacleGrid[i][j]==0 else 0
        return dp[0][0]