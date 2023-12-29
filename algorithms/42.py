from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left=[0 for i in range(len(height))]
        right=[0 for i in range(len(height))]
        lm=0
        rm=0
        v = 0
        for i in range(len(height)):
            if height[i]>lm:
                lm = height[i]
            left[i]=lm
            if height[-1-i]>rm:
                rm=height[-i-1]
            right[-1-i]=rm
        for i in range(1,len(height)-1):
            h=min(left[i], right[i])
            if h>height[i]:
                v+=(h-height[i])
        return v




height = [0,1,0,2,1,0,1,3]
s=Solution()
x=s.trap(height)
print(x)