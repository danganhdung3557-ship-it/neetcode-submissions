class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict_value = {}

        for word in strs:
            
            count = [0]*26 #create a hash map
            
            for letter in word:

                count[ord(letter) - ord("a")] += 1 # each letter has their values

            key = tuple(count) # dictionary accepts the tuple values
            
            if key not in dict_value:

                dict_value[key] = [] #add the key and value to dictionary
        
            dict_value[key].append(word)
        
        return list(dict_value.values())
    




