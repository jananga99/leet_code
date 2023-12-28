class Solution:
    def intToRoman(self, num: int) -> str:

        if num%10==9:
            roman="IX"
        elif(num%10>=5):
            roman="V"+"I"*(num%10-5)
        elif num%5==4:
            roman="IV"
        else:
            roman="I"*(num%5)

        if num%100>=90:
            roman="XC"+roman
        elif(num%100>=50):
            roman="L"+"X"*((num%100-50)//10)+roman
        elif num%50>=40:
            roman="XL"+roman
        else:
            roman="X"*((num%50)//10)+roman
        
        if num%1000>=900:
            roman="CM"+roman
        elif(num%1000>=500):
            roman="D"+"C"*((num%1000-500)//100)+roman
        elif num%500>=400:
            roman="CD"+roman
        else:
            roman="C"*((num%500)//100)+roman
        
        roman = "M" * (num//1000)+roman

        return roman
        
s=Solution()
for i in range(1, 4000):
    x=s.intToRoman(i)
    print(x)

# num = [
#     3,
#     58,
#     1994
# ]
# ans = [
#     "III",
#     "LVIII",
#     "MCMXCIV"
# ]
# for i in range(len(num)):
#     s = Solution()
#     x = s.intToRoman(num[i])
#     if x==ans[i]:
#         print("Pass")
#     else:
#         print(f"Fail {num[i]} expected {ans[i]} but got {x}")
