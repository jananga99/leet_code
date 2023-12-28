from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        def rec(nums, sub):
            out.append(sub)
            if nums:
                for i in range(len(nums)):
                    rec(nums[i+1:], sub+[nums[i]])
        rec(nums, [])
        return out
nums = [1,2,3]
s=Solution()
x=s.subsets(nums)
print(x)