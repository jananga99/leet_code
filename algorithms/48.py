from typing import List
from copy import deepcopy

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
                

matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
for r in matrix:
    o=""
    for c in r:
        o+=str(c)+" "
    print(o)
print()
s=Solution()
s.rotate(matrix)
for r in matrix:
    o=""
    for c in r:
        o+=str(c)+" "
    print(o)