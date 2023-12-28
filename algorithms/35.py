from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary(i,j):
            if i==j:
              
                if nums[i]>=target:
                    return i
                else:
                    return i+1
            mid=(i+j)//2
            if nums[mid]<=target:
                return binary(i,mid)
            else:
                return binary(mid+1, j)
        return binary(0, len(nums)-1)
    
arr = [1,3,5,6]
target=5
s=Solution()
x=s.searchInsert(arr, target)
print(x)