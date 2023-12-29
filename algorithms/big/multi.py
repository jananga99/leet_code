class Solution:
    def sum(self, arr):
        arr=list(filter(lambda x:x!="0",arr))
        if not arr:
            return "0"
        out = ""
        carry = 0
        keepGoing=True
        i=-1
        while keepGoing:
            keepGoing = False
            s=carry
            carry=0
            for x in arr:
                if len(x)>=-i:
                    keepGoing=True
                    s+=int(x[i])
            s=str(s)
            out=s[-1]+out
            if len(s)>1:
                carry=int(s[:-1])
            i-=1
        if out[0]=="0":
            out=out[1:]
        return out
    def multiply(self, num1: str, num2: str) -> str:
        def multiplyOneDigit(num:str, d:int):
            carry=0
            out=""
            for i in num[::-1]:
                t=str(carry+d*int(i))
                carry=0
                out=t[-1]+out
                if len(t)>1:
                    carry=int(t[:-1])
            if carry>0:
                out=str(carry)+out
            return out
        sumArr=list(map(lambda t: multiplyOneDigit(num1,int(t[1]))+"0"*t[0], enumerate(num2[::-1])))
        print(sumArr)
        x=self.sum(sumArr)
        return x

num1="408"
num2="5"
num3="49200"
s=Solution()
x=s.multiply(num1 ,num2)
print(x)
# x=s.sum(['738', '6150', '49200'])