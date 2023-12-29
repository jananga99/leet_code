# Math Tips

- In unique paths problem where you count the unique paths from top left corner to bottom left corner, 
  
  ```Maths
  Count=(m+n-2)C(m-1)

    ```Python3
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m+n-2, m-1)

- To find sqrt you can use binary search
  
```Python3

class Solution:
    def mySqrt(self, x: int) -> int:
        left,right=1,x
        while left<=right:
            mid=(left+right)//2
            if mid*mid==x:
                return mid
            if mid*mid>x:
                right=mid-1
            else:
                left=mid+1
        return right
