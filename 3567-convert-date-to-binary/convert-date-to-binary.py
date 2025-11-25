class Solution:
    def convertDateToBinary(self, date: str) -> str:
        str_list = date.split("-")
        res = ""
        print(str_list)
        for i in str_list:
            res+=bin(int(i))[2:]+"-"
        return res[0:len(res)-1]
        