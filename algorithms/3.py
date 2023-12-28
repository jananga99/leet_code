class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=len(s)
        if(l==0):
            return 0
        hashMap={}
        dp=[0 for i in range(l)]
        dp[0]=1 
        hashMap[s[0]] = 0
        for i in range(1, l):
            if hashMap.get(s[i]) is None:
                dp[i] = dp[i-1] +1
            else:
                dp[i] = i- max(hashMap[s[i]], i-1-dp[i-1])
            hashMap[s[i]] = i
        return max(dp)

s=[
    "abcabcbb",
    "bbbbb",
    "pwwkew",
    "",
    " ",
    "au",
    "dvdf",
    "abba"
]
ans=[
    3,
    1,
    3,
    0,
    1,
    2,
    3,
    2
]
print("string ans expected")
for i in range(len(s)):
    sol = Solution()
    x = sol.lengthOfLongestSubstring(s[i])
    if(x!=ans[i]):
        print(f"{s[i]} {x} {ans[i]}")