class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        neg = -1 if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0 else 1
        dividend=abs(dividend)
        divisor=abs(divisor)
        divisorCount=1
        while dividend>=(divisor<<1):
            divisor<<=1
            divisorCount<<=1
        quo=0
        while divisorCount>0:
            if dividend>=divisor:
                dividend-=divisor
                quo += divisorCount
            divisor>>=1
            divisorCount>>=1
        return quo*neg

s=Solution()
dividend=98
divisor=3
x=s.divide(dividend, divisor)
print(x)