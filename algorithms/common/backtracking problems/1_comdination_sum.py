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

    def combinationSumEasier(self, candidates: List[int], target: int) -> List[List[int]]:

        out = []
        def comb(candidates, target, sub):
            if candidates: 
                for ind,i in enumerate(candidates):
                    if target==i:
                        out.append(sub+[i])
                    elif target>i:
                        comb(candidates[ind:], target-i, sub+[i])
        comb(candidates, target, [])
        return out
candidates = [2,3,6,7]
target=7
s=Solution()
x=s.combinationSum(candidates, target)
print(x)