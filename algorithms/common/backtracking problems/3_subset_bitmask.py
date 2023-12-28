from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        out=[]
        for i in range(2**n,2**(n+1)):
            bitmask= bin(i)[3:]
            out.append(list(map(lambda x:x[1],filter(lambda t:bitmask[t[0]]=="1",enumerate(nums)))))
        return out
nums = [1,2,3]
s=Solution()
x=s.subsets(nums)
print(x)