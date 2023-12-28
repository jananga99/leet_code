class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        s = self.countAndSay(n-1)
        c=1
        out=""
        if len(s)==1 :
            out+="1"+s[0]
            return out
        for i in range(1, len(s)):
            if s[i]==s[i-1]:
                c+=1
            else:
                out+=str(c)+str(s[i-1])  
                c=1
        out+=str(c)+str(s[-1])
        return out
n=5
s=Solution()
x=s.countAndSay(n)
print(x)
# 1211