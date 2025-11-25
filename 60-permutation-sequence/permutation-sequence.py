from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = ""
        arr = list(permutations(range(1,n+1)))
        for i in arr[k-1]:
            res += str(i)
        return res