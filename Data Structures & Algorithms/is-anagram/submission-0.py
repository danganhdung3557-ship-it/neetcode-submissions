class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case (len is different)
        if len(s) != len(t):
            return False
        # Why?!
        return sorted(s) == sorted(t)



