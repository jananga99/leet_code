from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        diff = float('inf')
        closest = None
        for i in range(len(nums)):
            val = target - nums[i]
            a=i+1
            b=len(nums)-1
            while a<b:
                d = abs(target-nums[a]-nums[b]-nums[i]) 
                if d==0:
                    return target
                if d<diff:
                    diff=d
                    closest = nums[a]+nums[b]+nums[i]
                if target-nums[a]-nums[b]-nums[i]>0:
                    a+=1
                else:
                    b-=1
        return closest

        # closet = None
        # dist = float('inf')
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             s = nums[i]+nums[j]+nums[k] 
        #             if abs(target-s)<dist:
        #                 dist=abs(target-s)
        #                 closet = s
        # return closet

nums = [
    [-1,2,1,-4],
    [0,0,0]
]
target = [1,
          1
          ]
ans=[2,0]
s = Solution()
for i in range(len(nums)):
    x = s.threeSumClosest(nums[i], target[i])
    if x==ans[i]:
        print("Pass")
    else:
        print(f"Fail {nums[i]} {target[i]} expeted {ans[i]} git {x}")
            