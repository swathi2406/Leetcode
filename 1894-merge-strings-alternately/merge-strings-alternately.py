class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1Count = len(word1)
        word2Count = len(word2)
        word3 = ""
        for i in range(min(word1Count,word2Count)):
            word3 = word3 + word1[i] + word2[i]
        word3 = word3 + word1[i+1:] + word2[i+1:]
        return word3
