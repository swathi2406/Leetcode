class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in nums:
            if n in nums:
                n-=1
        return n
        