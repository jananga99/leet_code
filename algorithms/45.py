from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        reach, count, last = 0,0,0
        for i in range(len(nums)):
            if last>=len(nums)-1:
                return count
            reach=max(reach, i+nums[i])
            if i==last:
                count+=1
                last=reach


# nums = [2,3,1,1,4]
nums = 2,3,0,1,4
s=Solution()
x=s.jump(nums)
print(x)