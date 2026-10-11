class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        '''
        # edge case (len is different)
        if len(s) != len(t): # -> O(1)
            return False
        # Why?!
        return sorted(s) == sorted(t) #-> O(n.logn)
        

        '''
# write the code to O(n)

        #Create a empty dictionary
        dict_value = {}
        
        #Loop through s
        for s_letter in t:
            # if the s_letter is not in dictionary list
            if s_letter not in dict_value:
                dict_value[s_letter] = 1 
            #what if it is in
            else:
                dict_value[s_letter] += 1
        
        #Loop through t
        for t_letter in s:
            # if the t_letter is not in dictionary list
            if t_letter not in dict_value:
                return False
            #what if it is in
            else:
                dict_value[t_letter] -= 1
        
        #check the value inside the dictionaries
        for value in dict_value.values():
            #if the value is different from 0
            if value != 0:
                #return False
                return False
        #return True
        return True 




