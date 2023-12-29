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
        
    # BETTER
    def getPermutation(self, n: int, k: int) -> str:
        def next(s):
            j=len(s)-1
            while j>0 and s[j]<s[j-1]:
                j-=1
            if j==0:
                return s[::-1]
            j-=1
            i=len(s)-1
            while i>j and s[j]>=s[i]:
                i-=1
            s[i],s[j]=s[j],s[i]
            s=s[:j+1]+s[j+1:][::-1]
            return s
        a=[i+1 for i in range(n)]
        for i in range(k-1):
            a=next(a)
        return "".join(map(lambda x:str(x),a))

    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n+1)] # list of numbers from 1 to n
        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i-1] * i
        
        k -= 1
        result = []
        for i in range(n-1, -1, -1):
            index = k // factorial[i]
            result.append(str(nums[index]))
            nums.pop(index)
            k = k % factorial[i]
        
        return ''.join(result)

a=[1,2,3]
s=Solution()
s.nextPermutation(a)
print(a)
        