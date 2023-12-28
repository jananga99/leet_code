class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31-1
        MIN = -2**31
        if x >= 0:
            res = int(str(x)[::-1])
        else:
            res=int("-"+str(abs(x))[::-1])
        return res if MIN <= res <= MAX else 0