


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxArea = 0
        while i<=j:
            curArea = (j-i)*min(height[i],height[j])
            maxArea = max(maxArea,curArea)
            if height[i]<height[j]:
                i+=1
            elif height[j]<height[i]:
                j-=1
            else:
                i+=1
                j-=1
        return maxArea            

heights = [
    [1,8,6,2,5,4,8,3,7],
    [1,2]
]
ans = [
    49,
    1
]
for i in range(len(heights)):
    s = Solution()
    x=s.maxArea(heights[i])
    if x==ans[i]:
        print("Pass")
    else:
        print(f"Fail {heights[i]} expected {ans[i]} got {x}")