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
                    else:   # This also optimizes the code
                        break
            return out
        candidates.sort()
        return comb(candidates, target)