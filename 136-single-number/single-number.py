class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        freq_dict = {}
        for i in nums:
            if i in freq_dict.keys():
                freq_dict[i] +=1
            else:
                freq_dict[i] = 1
        for k,v in freq_dict.items():
            if v == 1:
                res = k
        return res