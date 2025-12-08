class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = int((high-low+1))
        if low == high:
            if low %2 !=0:
                return 1
            else:
                return 0
        else:
            if res %2 ==0:
                return res//2   
            else:
                if (high or low) %2 !=0:
                    return res//2  +1
                else:
                    return res//2 