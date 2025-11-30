class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_list = list(word1)
        word2_list = list(word2)
        j = 0
        for i in range(len(word2)):
            j+=1
            word1_list.insert(i+j,word2[i])
        res = ""
        for i in word1_list:
            res+=i
        return res