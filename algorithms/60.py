class Solution:
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
            print(i,j)
            s[i],s[j]=s[j],s[i]
            s=s[:j+1]+s[j+1:][::-1]
            return s
        a=[i+1 for i in range(n)]
        for i in range(k-1):
            a=next(a)
            print(a)
        return "".join(map(lambda x:str(x),a))

s=Solution()
n=3
x=s.getPermutation(n,3)
print(x)