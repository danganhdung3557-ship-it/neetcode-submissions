from functools import cache
class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        One_step = self.climbStairs(n-2)
        Two_step = self.climbStairs(n-1)
        return One_step + Two_step