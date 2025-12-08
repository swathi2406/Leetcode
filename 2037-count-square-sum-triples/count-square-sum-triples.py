import math
class Solution:
    def countTriples(self, n: int) -> int:
        ch = 0
        for i in range(1,n+1,1):
            lp,rp = 1,i-1
            # print(i," ",lp," ",rp)
            while lp < rp:
                if math.pow(i,2) == math.pow(lp,2) + math.pow(rp,2):
                    ch +=2
                    lp +=1
                    rp-=1
                elif math.pow(i,2) > math.pow(lp,2) + math.pow(rp,2):
                    lp+=1
                else:
                    rp-=1
        return ch