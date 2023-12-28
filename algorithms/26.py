class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        t = list(map(lambda x:nums[x],filter(lambda i:i==0 or nums[i]!=nums[i-1], range(len(nums)))))
        for i in range(len(t)):
            nums[i]=t[i]
        return len(t) 