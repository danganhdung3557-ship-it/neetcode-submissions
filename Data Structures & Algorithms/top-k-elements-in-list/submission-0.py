class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Create dictionary
        dict_value = {}

        #create the empty list
        list_output = []

        # iterate the integer inside the list
        for number in nums:
            # if number in dict_value add in dict_value
            if number in dict_value:
                dict_value[number] += 1
            #if number is not in dict_value we add the number for value = 1
            else:
                dict_value[number] = 1
        # check the value whether it is larger than k?
        '''
        for frequent_of_num in dict_value.values():

            if frequent_of_num >= k:
                list_output.append(dict_value[number])

                return list_output
        '''
        # chatgpt fix the problem
        for i in range(k):
            most_frequent = max(dict_value, key=dict_value.get)

            list_output.append(most_frequent)

            del dict_value[most_frequent]

        return list_output
        