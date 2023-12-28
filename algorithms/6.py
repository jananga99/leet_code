class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        arr = ["" for i in range(numRows)]
        t1 = 2*numRows-2
        for i,e in enumerate(s):
            t = i%t1 
            if t<numRows:
                arr[t]+=e
            else:
                arr[t1-t]+=e
        return "".join(arr)
s = [
    "PAYPALISHIRING",
    "PAYPALISHIRING",
    "A"
]
numRows = [
    3,
    4,
    1
]
ans = [
    "PAHNAPLSIIGYIR",
    "PINALSIGYAHRPI",
    "A"
]
for i in range(len(ans)):
    r = Solution().convert(s[i], numRows[i])
    if r == ans[i]:
        print("Pass")
    else:
        print("Fail!!!")
        print(s[i],numRows,"Expected:", ans[i], "but got:", r)
        