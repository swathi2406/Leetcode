import math
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return int(sum(nums) % k)
        