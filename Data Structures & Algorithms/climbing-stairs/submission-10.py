class Solution:
    #Memoization BOTTOM UP/ using dictionary data type
    #memo = {}
    def climbStairs(self, n: int) -> int:
        '''
        if n in self.memo:
            return self.memo[n]

        if n == 1 or n == 2:
            return n

        res = self.climbStairs(n-2) + self.climbStairs(n-1)
        
        self.memo[n] = res
        return res
        '''

#Solve the question through method "TOP DOWN APPROACH"
        #create the empty list
        empty_list = []
        
        # add 2 numbers inside the list
        empty_list.append(1)
        empty_list.append(2)

        # if n <= 2:
        #     return n

        for i in range(2, n):
            empty_list.append(empty_list[i - 1] + empty_list[i - 2])
        
        return empty_list[n - 1]

        