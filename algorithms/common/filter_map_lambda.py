from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums = list(map(lambda x:nums[x],filter(lambda i:i==0 or nums[i]!=nums[i-1], range(len(nums)))))
        return len(nums)