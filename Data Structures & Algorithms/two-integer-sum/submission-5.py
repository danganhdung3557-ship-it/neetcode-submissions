class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        for i in range(len(nums)): # -> O(n)
            for j in range(i + 1, len(nums)): #--- O(n x n)
                if nums[i] + nums[j] == target:
                    return [i, j]
        '''






#How to turn this code into O(n)

#Using AI to help turning the code into O(n) --> Chatgpt
        # AI recommend using dictionaries which is faster than using normal list
        
        # hashmap
        num_to_index = {}

        #loop 
        for i in range(len(nums)):
            difference = target - nums[i]

            
            if difference in num_to_index:
                #if difference are existed in the dictionary
                #return the list of index
                return [num_to_index[difference],i]
            
            # if difference doesn't exist in num_to_index
            # add that number as key and its index as value 
            num_to_index[nums[i]] = i










    

        