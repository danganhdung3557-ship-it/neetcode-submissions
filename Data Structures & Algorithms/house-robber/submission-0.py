class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Using Bottom Up strategies to solve the problem

        Regulation:
        You cannot rob TWO ADJACENT HOUSES

        Example: 
        [2] -> take the first house result = 2
        [2,9] -> take the second house -> result = 9
        [2,9,8] -> We will rob the first and third one -> [9,10] -> result = 10
        [2,9,8,3] -> We will rob the second and fourth one -> [9,3] -> result = 12
        [2,9,8,3,6] -> We will rob first, third, sixth one -> [2,8,6] > [9,3] -> result = 16

        Formula:
        max(dp[i - 1], nums[i] + dp[i - 2])
        '''

        # initialize n in length of the list nums
        n = len(nums)

        #base condition for the bottom up
        if n == 1:
            return nums[0]

        #if the list has 2 number take the highest 1 inside the list
        if n == 2:
            return max(nums[0], nums[1])
        
        #memoization
        memo = {0:nums[0], 1:max(nums[0],nums[1])}

        def helper(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = max(nums[i]+helper(i-2), helper(i-1))
                return memo[i]

        return helper(n-1)


                
