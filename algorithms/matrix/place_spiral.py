class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        out=[[None for j in range(n)] for i in range(n)]
        upper=left=0
        lower=right=n-1
        d=n
        c=1
        while upper<=lower:
            for i in range(left, right+1):
                out[upper][i]=c
                c+=1
            upper+=1
            for i in range(upper, lower+1):
                out[i][right]=c
                c+=1
            right-=1
            for i in range(right, left-1,-1):
                out[lower][i]=c
                c+=1
            lower-=1
            for i in range(lower, upper-1, -1):
                out[i][left] = c
                c+=1
            left+=1
        return out