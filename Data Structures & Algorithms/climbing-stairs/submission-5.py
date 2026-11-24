class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        pre1 = 1
        pre2 = 2

        for i in range(3, n+1):
            tmp = pre1 + pre2
            pre1 = pre2 
            pre2 = tmp
        
        return pre2