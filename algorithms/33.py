from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(i,j):
            if j<i:
                return -1
            if i==j:
                return i if nums[i]==target else -1
            if nums[i]==target:
                return i
            if nums[j]==target:
                return j
            mid=(i+j)//2
            if nums[mid]==target:
                return mid
            
            if nums[i]<nums[mid]:
                if nums[i]<target<nums[mid]:
                    return binary(i,mid)
                else:
                    return binary(mid+1,j)
            else:
                if nums[j]>target>nums[mid]:
                    return binary(mid+1, j)
                else:
                    return binary(i+1, mid)
            
        return binary(0, len(nums)-1)