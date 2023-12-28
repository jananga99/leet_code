from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        n = len(nums)
        def rec(nums, sub):
            if len(sub)==n:
                out.append(sub)
            elif nums:
                for i in range(len(nums)):
                    rec(nums[:i]+nums[i+1:], sub+[nums[i]])
        rec(nums, [])
        return out
nums = [1,2,3]
s=Solution()
x=s.permute(nums)
print(x)