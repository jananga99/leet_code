class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not bool(digits):
            return []
        hashMap = {}
        hashMap['2']="abc"
        hashMap['3']="def"
        hashMap['4']="ghi"
        hashMap['5']="jkl"
        hashMap['6']="mno"
        hashMap['7']="pqrs"
        hashMap['8']="tuv"
        hashMap['9']="wxyz"
        out=[""]
        for d in digits:
            temp = out
            out = []
            for i in hashMap[d]:
                for t in temp:
                    out.append(t+i)
        return out