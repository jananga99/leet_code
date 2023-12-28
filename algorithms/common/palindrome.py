def isPalindrome(self, x: int) -> bool:
    x = str(x)
    for i in range(len(x)//2):
        if x[i]!=x[-i-1]:
            return False
    return True


def expand(s, i,j):
    while i>=0 and j<len(s) and s[i]==s[j]:
        i-=1
        j+=1
    return j-1-i
