from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        def comb(candidates, target, sub):
            if not candidates or target<candidates[0]: # This greatly optimizes the code
                return 
            for ind,i in enumerate(candidates):
                if ind==0 or candidates[ind]!=candidates[ind-1]:
                    if target==i:
                        out.append(sub+[i])
                    elif target>i:
                        comb(candidates[ind+1:], target-i, sub+[i])
                    else:   # This also optimizes the code
                        break
        candidates.sort()
        comb(candidates, target, [])
        return out

candidates = [10,1,2,7,6,1,5]
target = 8
s=Solution()
x = s.combinationSum2(candidates, target)
print(x)