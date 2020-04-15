class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        return_list = []
        dic_anas = {}
        for strc in strs:
            strc_s = "".join(sorted(strc))
            if strc_s in dic_anas:
                dic_anas[strc_s].append(strc)
            else:
                dic_anas[strc_s] = [strc]
        for list_str in dic_anas:
            return_list.append(dic_anas[list_str])

        return return_list

s=Solution()

input_data = ["eat", "tea", "tan", "ate", "nat", "bat"] #groupAnagrams
print(s.groupAnagrams(input_data))