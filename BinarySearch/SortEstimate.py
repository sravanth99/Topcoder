import math
class SortEstimate:
    def  howMany(self,c,time):
        lo = 1+1e-14
        hi = 10**8+1e-14
        while(hi/lo > 1+1e-14):
            #print(lo,hi)
            mid = (hi+lo)/2
            if c*(math.log(mid)/math.log(2))*mid <= time:
                lo = mid
            else:
                hi = mid
        return lo