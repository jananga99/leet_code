class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        def expand(i,j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
            return j-1-i
        maxStr = (0,0)
        for i in range(l):
            odd = expand(i, i)
            if odd > maxStr[1]-maxStr[0]+1:
                dist = odd//2
                maxStr = (i-dist,i+dist)
            even = expand(i,i+1)
            if even > maxStr[1]-maxStr[0]+1:
                dist = even//2-1
                maxStr = (i-dist, i+1+dist)
        return s[maxStr[0]:1+maxStr[1]]
        # l = len(s)
        # maxStr = ""
        # for i in range(l):
        #     for j in range(i+len(maxStr),l):
        #         cur = s[i:j+1]
        #         isPalindrome = True
        #         for k in range(len(cur)//2):
        #             if cur[k]!=cur[len(cur)-k-1]:
        #                 isPalindrome = False
        #                 break
        #         if isPalindrome:
        #             maxStr = cur
        # return maxStr
        # l=len(s)
        # if l==0:
        #     return ""
        # strs = [s[0]]
        # maxStr = s[0]
        # for i in range(1, l):
        #     print(strs)
        #     newStrs=[s[i]]
        #     for ss in strs:
        #         if len(ss)==1:

        #         if len(ss)<i and s[i]==s[i-1-len(ss)]:
        #             newStr = s[i-1-len(ss):i+1]
        #             newStrs.append(newStr)
        #             if len(newStr)>len(maxStr):
        #                 maxStr = newStr
        #     strs = newStrs
        # return maxStr                        
        # dpSame = [1 for i in range(l)]
        # dpDiff = [1 for i in range(l)]
        # maxStr = s[0]
        # for i in range(1,l):
        #     if(s[i]==s[i-1]):
        #         dpSame[i] = dpSame[i-1]+1
        #         if i-1-dpDiff[i-1]>=0:
        #             dpDiff[i] = dpDiff[i-1]+2 if s[i]==s[i-1-dpDiff[i-1]] else 1
        #     else:
        #         dpSame[i] = 1
        #         newSame = dpSame[i-1]+2 if s[i]==s[i-1-dpSame[i-1]] else 1
        #         newDiff = dpDiff[i-1]+2 if s[i]==s[i-1-dpDiff[i-1]] else 1
        #         dpDiff[i] = max(newSame, newDiff)
        #     m  =  max(dpSame[i], dpDiff[i])
        #     if m>len(maxStr):
        #         maxStr = s[i+1-m:i+1]
        # return maxStr



# print("s  ans  expeced")
s = [
    "babad",
    "cbbd",
    "a",
    "ac",
    "bb",
    "ccc",
    "aaaa",
]
ans = [
    "bab",
    "bb",
    "a",
    "a",
    "bb",
    "ccc",
    "aaaa",
]
for i in range(len(s)):
    r = Solution().longestPalindrome(s[i])
    if(r != ans[i]):
        print(s[i], r, ans[i])
