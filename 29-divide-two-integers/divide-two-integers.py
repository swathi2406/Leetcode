class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = dividend/divisor
        if math.pow(-2,31) > res:
            return math.trunc(math.pow(-2,31))
        elif res > math.pow(2,31)-1:
            return math.trunc(math.pow(2,31) -1)
        return math.trunc(res)
        