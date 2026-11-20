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

        TIME: O(n) + O(mlogn) + O(n) -> O(n + mlogn)

        Sorting:
                act, cat --> act, act same words -> Group
        stop, pots, tops ---> same words -> Group

        What is hashmap?
        cat : cat, act
        stop: stop, pots, tops

        Hashing:
        
        '''

        # Make a empty dictionary and this contain a group anagrams

        #group = {}

        #iterate words inside the list
        #for word in strs: #--> O(n); n: size of list strs
            
            # after that we will need to sort the word
            #word_sorted = sorted(word) #-> O(m.logm); m: size of strings
            #after sort the word into the each of word
            #in this time I will try to connect each letter together to create the same characters
            #same_character_word = ''.join(word_sorted)
            #word_sorted = tuple(word_sorted) #-> O(1)
            #Make a condition to create a list inside the dictionary for the word which is not already inside dict
            #if word_sorted not in group: #-> hashmap figures out the key = O(1)
                #group[word_sorted] = []
            
            #otherwise if it is already inside append that word with same character inside the list
            #group[word_sorted].append(word)

        #return the result for the group anagram and get the value inside the list
        #return list(group.values())

        dict_value = {}  #-> mapping charcount to list of anagrams 
#-> O(n.m.logm)
        for word in strs:
            '''
            What is the method that minimize the time complexity?
            method without "Sort" the strings.
            '''       
            count = [0] * 26 #-> hash map each letter from 0 -> 25
            
            # now we iterate each letter in word
            for letter in word:
                # and now we want to set the key for each letter
                # ord("a") is 97 -> called Unicode
                count[ord(letter) - ord("a")] += 1
            
            # count into a tuple and set it as a key
            key = tuple(count)
            
            #condition to add count as a key # -> add the count into a dict_value and we know in python dictionaries is immutable.   
            if key not in dict_value:
                dict_value[key] = []

            # append word with that key
            dict_value[key].append(word)

        return list(dict_value.values())

            


























