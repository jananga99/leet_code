from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def comb(candidates, target):
            out=[]
            if not candidates or target<candidates[0]: # This greatly optimizes the code
                return out
            for ind,i in enumerate(candidates):
                if ind==0 or candidates[ind]!=candidates[ind-1]:
                    if target==i:
                        out.append([i])
                    elif target>i:
                        t=comb(candidates[ind+1:], target-i)
                        for j in t:
                            out.append(j+[i])
            return out
        candidates.sort()
        return comb(candidates, target)

candidates = [10,1,2,7,6,1,5]
target = 8
s=Solution()
x = s.combinationSum2(candidates, target)
print(x)