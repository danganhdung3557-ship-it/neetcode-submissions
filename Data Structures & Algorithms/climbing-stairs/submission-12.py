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

        memo = {1:1,2:2} # memo is a dictionary where we can have key and value
        
        # using function
        def fib(n):

            # This condition when n is already in memo
            if n in memo:
                return memo[n]
            
            #Reverse if n is not in memo
            else:
                memo[n]= fib(n - 1) + fib(n - 2)

                return memo[n]

        return fib(n)
