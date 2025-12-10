class Solution:
    def reverseBits(self, n: int) -> int:
        binary_form = str.zfill(bin(n)[2:],32)
        reversed_bin = binary_form[::-1]
        return int(reversed_bin,2)