from ast import List

# Run time 55ms
# Beats 94.84%of users with Python3

class Solution:
    def twoSum(self, nums, target) :
        hashMap = {}
        for i in range(len(nums)):
            comp = target-nums[i]
            j = hashMap.get(comp) 
            if(j is not None):
                return [j,i]
            hashMap[nums[i]] = i 




nums = [
    [2,7,11,15],
    [3,2,4],
    [3,3]
]
target = [
    9,
    6,
    6
]
ans = [
    [0,1],
    [1,2],
    [0,1]  
]
print("nums target ans expected")
for i in range(len(nums)):
    sol = Solution()
    x = sol.twoSum(nums[i],target[i])
    if(x!=ans[i]):
        print(f"{nums[i]} {target} {x} {ans[i]}")
