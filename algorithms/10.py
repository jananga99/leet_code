class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]
        

# Recursive Solution
    #    def isMatch(self, string: str, pattern: str) -> bool:
    #     if not pattern:
    #         return not string
    #     first_match = bool(string) and pattern[0] in (".",string[0])
    #     if len(pattern)>=2 and pattern[1]=="*":
    #         return self.isMatch(string, pattern[2:]) or first_match and self.isMatch(string[1:], pattern)
    #     else:
    #         return first_match and self.isMatch(string[1:], pattern[1:])     

s=[
    "aa",
    "aa",
    "ab"
]
p=[
    "a",
    "a*",
    ".*"
]
ans=[
    False,
    True,
    True
]
for i in range(len(ans)):
    r = Solution().isMatch(s[i], p[i])
    if r == ans[i]:
        print("Pass")
    else:
        print("Fail!!!")
        print(s[i],p[i],"Expected:", ans[i], "but got:", r)
