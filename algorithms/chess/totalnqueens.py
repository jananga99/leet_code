class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        visited_cols=set()
        visited_diagonals=set()
        visited_antidiagonals=set()
        tt=[]
        def backtrack(r):
            if r==n:                
                tt.append(1)
                return
            for c in range(n):
                diff=r-c
                _sum=r+c
                if not (c in visited_cols or diff in visited_diagonals or _sum in visited_antidiagonals):                    
                    visited_cols.add(c)
                    visited_diagonals.add(diff)
                    visited_antidiagonals.add(_sum)
                    backtrack(r+1) 

                    # reset the path
                    visited_cols.remove(c)
                    visited_diagonals.remove(diff)
                    visited_antidiagonals.remove(_sum)
                            
        backtrack(0)
        return len(tt)