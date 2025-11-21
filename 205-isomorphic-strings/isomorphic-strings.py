class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ch = True
        if len(s) != len(t):
            ch = False
            return ch
        map_dict = {}
        j = 0
        for i in s:
            if i not in map_dict.keys():
                if t[j] in map_dict.values() and i != map_dict.get(t[j]):
                    ch = False
                    return ch
                else:
                     map_dict[i]= t[j]
                # print(j)
            else:
                if map_dict[i] != t[j]:
                    ch = False
            j = j+1
        return ch