class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        What is 32-bit integer?

        each product is guaranteed to fit in a 32-bit integer

        range:
        minimum of 32bit-integer = -2**31
        maximum of 32bit-integer = 2**31 - 1


        '''

        #initialized the prefix
        prefix = 1
        suffix = 1

        res = [] #-> [1, 1, 2, 8]

        for num in nums:
            
            res.append(prefix)

            prefix *= num #multiply with the nums[i]

        for j in range(len(nums)-1, -1, -1):

            res[j] *= suffix

            suffix *= nums[j] # suffix multiply with list nums reversed

        return res
                






