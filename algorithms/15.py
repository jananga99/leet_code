from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        positiveHash = {}
        negativeHash = {}
        zeroCount = 0
        ans = []
        for n in nums:
            if n==0:
                zeroCount+=1
            elif n>0:
                if positiveHash.get(n) is None:
                    positiveHash[n]=1
                else:
                    positiveHash[n]+=1
            else:
                if negativeHash.get(n) is None:
                    negativeHash[n]=1
                else:
                    negativeHash[n]+=1
        if zeroCount>=3:
            ans.append([0,0,0])
        positiveNums = list(positiveHash.keys())
        negativeNums = list(negativeHash.keys())
        for i in range(len(positiveNums)):
            if zeroCount>0 and negativeHash.get(-positiveNums[i]) is not None:
                ans.append([positiveNums[i], 0, -positiveNums[i]])
            if positiveHash[positiveNums[i]]>=2 and negativeHash.get(-2*positiveNums[i]) is not None:
                ans.append([positiveNums[i], positiveNums[i], -2*positiveNums[i]])
            for j in range(i+1, len(positiveNums)):
                if negativeHash.get(-positiveNums[i]-positiveNums[j]) is not None:
                    ans.append([positiveNums[i], positiveNums[j], -positiveNums[i]-positiveNums[j]])
        for i in range(len(negativeNums)):
            if negativeHash[negativeNums[i]]>=2 and positiveHash.get(-2*negativeNums[i]) is not None:
                ans.append([negativeNums[i], negativeNums[i], -2*negativeNums[i]])
            for j in range(i+1, len(negativeNums)):
                if positiveHash.get(-negativeNums[i]-negativeNums[j]) is not None:
                    ans.append([negativeNums[i], negativeNums[j], -negativeNums[i]-negativeNums[j]])        
        return ans
nums = [
    [-1,0,1,2,-1,-4],
    [0,1,1],
    [0,0,0]

]
s=Solution()
for i in range(len(nums)):
    print(nums[i])
    print(s.threeSum(nums[i]))