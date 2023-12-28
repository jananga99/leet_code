from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 4)

    def kSum(self, nums: List[int], target:int, k:int) -> List[List[int]]:
        if not nums:
            return []
        averageValue = target//k
        if averageValue < nums[0] or nums[-1] < averageValue:
            return []
        if k==2:
            return self.twoSum(nums, target)
        out = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            t = self.kSum(nums[i+1:], target-nums[i], k-1)
            for j in t:
                out.append(j+[nums[i]])
        return out

    def twoSum(self, nums: List[int], target:int)->List[List[int]]:
        a=0
        b=len(nums)-1
        out = []
        while a<b:
            v = nums[a]+nums[b]
            if v==target:
                out.append([nums[a],nums[b]])
                a+=1
            if v<target:
                a+=1
            else:
                b-=1
            while a<len(nums) and a>0 and nums[a]==nums[a-1]:
                a+=1
            while b>0 and b<len(nums)-1 and nums[b]==nums[b+1]:
                b-=1
        return out
        
k = 4
# nums = [1,0,-1,0,-2,2]
# nums = [-3,-2,-1,0,0,1,2,3]
nums = [-2,-1,-1,1,1,2,2]
target=0
s= Solution()
x = s.fourSum(nums, target)
print(x)