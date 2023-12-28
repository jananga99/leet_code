from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        def rec(nums, sub):
            out.append(sub)
            if nums:
                for i in range(len(nums)):
                    if i==0 or nums[i]!=nums[i-1]:
                        rec(nums[i+1:], sub+[nums[i]])
        rec(nums, [])
        return out
nums = [1,2,2]
s=Solution()
x=s.subsetsWithDup(nums)
print(x)