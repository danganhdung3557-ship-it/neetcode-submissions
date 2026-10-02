class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memory = []
        for n in nums:
            if n in memory:
                return True
            memory.append(n)
        return False
            
        
        









