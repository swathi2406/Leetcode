class Solution:
    def maxDistinct(self, s: str) -> int:
        count = 0
        for strs in "abcdefghijklmnopqrstuvwxyz":
            if strs in s:
                count +=1
        return count
        