class Solution:
    def maxDistinct(self, s: str) -> int:
        dict_freq_substring = {}
        count = 0
        for i in s:
            if i in dict_freq_substring.keys():
                dict_freq_substring[i] +=1
            else:
                dict_freq_substring[i] = 1
        for strs in dict_freq_substring.keys():
            count +=1
        return count
        