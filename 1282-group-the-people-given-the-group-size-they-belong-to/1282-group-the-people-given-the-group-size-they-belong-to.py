class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        dict_of_lists = {}
        for idx, val in enumerate(groupSizes):
            if val in dict_of_lists.keys():
                last_list = dict_of_lists[val][-1]
                if val > len(last_list):
                    last_list.append(idx)
                elif val == len(last_list):
                    dict_of_lists[val].append([idx])
            else:
                dict_of_lists[val] = [[idx]]
        
        res_list = []
        for key in dict_of_lists:
            for elem in dict_of_lists[key]:
                res_list.append(elem)
        return res_list