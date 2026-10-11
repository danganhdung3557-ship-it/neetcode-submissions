class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # create a empty list
        empty_list = set()

        #loop through the List[int]
        for i in range(len(nums)):

            #if the nums[i] (List[int]) inside the empty_list
            if nums[i] in empty_list:

                #return True
                return True

            #if "empty_list" did not have number --> add number
            empty_list.add(nums[i])
        
        #what if keep adding different number return False
        return False