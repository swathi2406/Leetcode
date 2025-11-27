class Solution:
    def countBits(self, n: int) -> list[int]:
        res = []
        # print(bin(n)[2:])
        for i in range(n+1):
            # print(str(bin(i)[2:]).count("1"))
            res.append(str(bin(i)[2:]).count("1"))
        return res
