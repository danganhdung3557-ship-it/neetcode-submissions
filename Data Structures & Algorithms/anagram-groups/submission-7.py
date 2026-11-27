class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        '''
        Group anagram -> hashmap in dictionary follows by each letter
        '''

        dict_value = {} #empty dictionary / using hashmap

        for word in strs: #iterate each word in strs: list[str]

            count = [0]*26 # 26 letters in table

            for letter in word: #iterate each letter in word

                count[ord(letter) - ord("a")] += 1  #get unicode for each letter

            key = tuple(count) #dictionary unable to have mutable key

            #assumption: key are not in dict_value
            if key not in dict_value:
                dict_value[key] = [] # add the key to the dict_value = dictionary

            dict_value[key].append(word) # add word to the dictionary as a key
        
        return list(dict_value.values())

