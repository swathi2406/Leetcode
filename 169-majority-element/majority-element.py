class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min = len(nums)//2
        dict_ = {}
        for i in nums:
            dict_[i] = 1+dict_.get(i,0)
            if dict_[i] >min:
                return i