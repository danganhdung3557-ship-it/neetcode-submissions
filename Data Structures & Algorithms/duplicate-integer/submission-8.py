class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memory = set()
        for n in nums:
            if n in memory:
                return True
            memory.add(n)
        return False
            
        
        









