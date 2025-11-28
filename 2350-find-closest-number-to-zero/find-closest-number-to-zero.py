class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort() #[-4,-2,1,4,8]
        max = nums[0] #-4
        for i in nums: #i = 1
            dis = math.dist([max],[0]) # 4
            if dis >= math.dist([i],[0]): # dist = 4 and math dist = 2
                max = i # max = -2
            else:
                continue

        return max
        