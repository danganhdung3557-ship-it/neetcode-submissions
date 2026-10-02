class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #for i in range(len(nums)):
            #for j in range(i + 1, len(nums)): #--- O(n^2)
                #if nums[i] + nums[j] == target:
                    #return [i, j]

#How to turn this code into O(n)

#Using AI to help turning the code into O(n) --> Chatgpt
        # AI recommend using dictionaries which is faster than using normal list

        # List recommend nums = [2,7,8,9] --> target: 9
        numbers = {} #-> [0, ]
        
        #Make a loop to count the number
        for i in range(len(nums)):
            _difnum_ = target - nums[i]

            if _difnum_ in numbers:
                return [numbers[_difnum_], i]

            numbers[nums[i]] = i #---> dictionaries use key and value to store memories.





    

        