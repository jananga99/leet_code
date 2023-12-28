class Solution:
    def romanToInt(self, s: str) -> int:
        s=s[::-1]
        num=0
        hashMap={}
        hashMap["I"]=1
        hashMap["V"]=5
        hashMap["X"]=10
        hashMap["L"]=50
        hashMap["C"]=100
        hashMap["D"]=500
        hashMap["M"]=1000
        for i,e in enumerate(s):
            if i>0 and s[i-1:i+1] in ["VI","XI","LX", "CX", "DC", "MC"]:
                num-=hashMap[e]
            else:
                num+=hashMap[e] 
        return num   
            
        