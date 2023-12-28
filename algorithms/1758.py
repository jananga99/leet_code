class Solution:
    def minOperations(self, s: str) -> int:
        if(len(s)==0):
            return 0
        x = s[::2].count("0" if s[0]=="1" else "1")+s[1::2].count(s[0])
        return min(x,len(s)-x)


s = [
    "0100",
    "10",
    "1111",
    "10010100"
]
ans = [
    1,
    0,
    2,
    3
]
for i in range(len(s)):
    sol = Solution()
    x = sol.minOperations(s[i])
    if(x!=ans[i]):
        print(f"error for {s[i]} {x} {ans[i]}")
