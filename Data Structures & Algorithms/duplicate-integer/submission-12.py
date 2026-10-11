class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # create a empty list
        empty_list = set()

        #Condition
        for i in range(len(nums)):
            if nums[i] in empty_list:
                return True
            empty_list.add(nums[i])
        return False