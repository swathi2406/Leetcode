class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dict_index = {}
        for i in range(len(nums)):
            if nums[i] in dict_index and abs(i - dict_index[nums[i]]) <=k:
                return True
            else:
                dict_index[nums[i]] = i
        return False
