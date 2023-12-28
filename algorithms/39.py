from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out=[]
        for ind,i in enumerate(candidates):
            if target==i:
                out.append([i])
            elif target>i:
                t=self.combinationSum(candidates[ind:], target-i)
                for j in t:
                    out.append(j+[i])
        return out
candidates = [2,3,6,7]
target=7
s=Solution()
x=s.combinationSum(candidates, target)
print(x)