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
        group = {}

        for word in strs:

            #This code print out the list of words
            word_sorted = "".join(sorted(word))
            '''
            "eat"
            ↓
            ['e', 'a', 't']     sorted()
            ↓
            ['a', 'e', 't']     join()
            ↓
            "aet"
            '''

            #Make a condition
            if word_sorted not in group:
                group[word_sorted] = []
            
            # Add the letter
            group[word_sorted].append(word)

        #return
        return list(group.values())