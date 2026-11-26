class Solution:
    '''
    Encode and Decode -> Encode is from list of strings
    to a string. Meanwhile, Decode is from strings to list of strings
    '''
    def encode(self, strs: List[str]) -> str:

        #create empty where we will join to have a string
        strings = []
        
        #iterate the list of string
        
        for word in strs:
            
            #length of the word
            length = len(word)

            #append the word into a list strings
            strings.append(f"{length}#{word}")
        
        return "".join(strings)

        
    def decode(self, s: str) -> List[str]:

        '''
        The concept of decode is from the strings -> list of
        strings

        if we have "5#Hello5#World" -> return ["Hello","World"]

        The question is how do we do this?

        5#Hello5#World has "5" and "#"
        '''

        #create a list word
        decoded_strs = []
        
        # starting with index 0
        i = 0
        
        while i < len(s):
            
            #end of the string
            j = i

            while s[j] != "#":
                j += 1

            #length of the word
            length = int(s[i:j])

            i = j + 1

            #add the word to the list
            decoded_strs.append(s[i:i + length])

            i = i + length
        
        return decoded_strs
        
            



