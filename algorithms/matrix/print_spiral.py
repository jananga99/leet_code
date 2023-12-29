class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        upper=left=0
        lower=len(matrix)-1
        right=len(matrix[0])-1
        out=[]
        while upper<=lower and left<=right:
            singleRow=upper==lower
            singleColumn=left==right
            for i in range(left, right+1):
                out.append(matrix[upper][i])
            upper+=1
            for i in range(upper, lower+1):
                out.append(matrix[i][right])
            right-=1
            if not singleRow:
                for i in range(right, left-1, -1):
                    out.append(matrix[lower][i])
                lower-=1
            if not singleColumn:
                for i in range(lower, upper-1, -1):
                    out.append(matrix[i][left])
                left+=1
        return out