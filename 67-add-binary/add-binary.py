class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_int = int(a,2)
        b_int = int(b,2)
        c_int = a_int+b_int
        return bin(c_int)[2:]