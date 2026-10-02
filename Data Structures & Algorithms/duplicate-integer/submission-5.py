class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        me = set()
        for Na in nums:
            if Na in me:
                return True
            nums = me.add(Na)
        return False
            
        
        









