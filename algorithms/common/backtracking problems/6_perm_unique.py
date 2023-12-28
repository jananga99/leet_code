from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        n = len(nums)
        def rec(nums, sub):
            if len(sub)==n:
                out.append(sub)
            elif nums:
                for i in range(len(nums)):
                    if i==0 or nums[i]!=nums[i-1]:
                        rec(nums[:i]+nums[i+1:], sub+[nums[i]])
        rec(nums, [])
        return out
nums = [1,1,2]
s=Solution()
x=s.permuteUnique(nums)
print(x)