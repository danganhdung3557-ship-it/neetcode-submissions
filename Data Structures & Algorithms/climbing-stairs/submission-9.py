class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]

        if n == 1 or n == 2:
            return n

        res = self.climbStairs(n-2) + self.climbStairs(n-1)
        
        self.memo[n] = res
        return res
#Solve the question through method "TOP DOWN APPROACH"
#Memoization BOTTOM UP

        