from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                for j in range(len(nums)-1, i,-1):
                    if nums[i]<nums[j]:
                        nums[i],nums[j]=nums[j],nums[i]
                        break
                t=nums[i+1:][::-1]
                for j in range(i+1, len(nums)):
                    nums[j]=t[j-i-1]
                break
        else:
            nums.reverse()
        

a=[1,2,3]
s=Solution()
s.nextPermutation(a)
print(a)
        