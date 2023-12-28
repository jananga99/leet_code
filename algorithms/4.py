from ast import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1 = 0
        p2 = 0
        m = len(nums1)
        n = len(nums2)
        upper = (m+n)/2

num1s = [
    [1,3],
    [1,2]
]

num2s = [
    [2],
    [3,4]
]

ans = [
    2,
    2.5
]
print("num1 num2 ans expected")
for i in range(len(num1s)):
    sol = Solution()
    x = sol.findMedianSortedArrays(num1s[i], num2s[i])
    if(x!=ans[i]):
        print(f"{num1s[i]} {num2s[i]} {x} {ans[i]}")