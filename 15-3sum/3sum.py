class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = [] # Use a list for results, and handle duplicates later or use set initially
        nums.sort()
        
        for i in range(len(nums) - 2): # Iterate up to len-3 because we need two more elements
            # Skip duplicate for 'i'
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicates for 'left' pointer
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    # Skip duplicates for 'right' pointer
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif current_sum < 0:
                    left += 1 # Need a larger sum
                else:
                    right -= 1 # Need a smaller sum
                    
        return res