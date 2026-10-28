class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Case:
        strs = ["act","pots","tops","cat","stop","hat"]

        strs = ["x"]

        strs = [""]

        Solution:
        1. Initialize the Dict with anagrams
        2. Loop through the list
        3. Sort the group and insert into a group
        4. Iterate through dict values and append the output

        Sorting:
                act, cat --> act, act same words -> Group
        stop, pots, tops ---> same words -> Group

        What is hashmap?
        cat : cat, act
        stop: stop, pots, tops

        Hashing:
        
        '''

        # Make a empty dictionary and this contain a group anagrams

        group = {}

        #iterate words inside the list
        for word in strs:
            
            # after that we will need to sort the word
            word_sorted = sorted(word)

            #after sort the word into the each of word
            #in this time I will try to connect each letter together to create the same characters
            same_character_word = ''.join(word_sorted)

            #Make a condition to create a list inside the dictionary for the word which is not already inside dict
            if same_character_word not in group:
                group[same_character_word] = []
            
            #otherwise if it is already inside append that word with same character inside the list
            group[same_character_word].append(word)

        #return the result for the group anagram and get the value inside the list
        return list(group.values())

            





























