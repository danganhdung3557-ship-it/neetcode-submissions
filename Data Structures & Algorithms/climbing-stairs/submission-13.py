class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        if n = 5 -> there are 2 arrays
        5 -> 4 and 3 -> this is top down methods
        otherwise 4 -> 3 and 2 and 3 -> 2 and 1.
                    5
                4       3
            3      2  2    1
        2      1                

        This methods repeat the arrays for 2 times then we need to use memozation
        '''

        # I will use dynamic programming
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0]*n
        dp[0] = 1
        dp[1] = 2

        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]
