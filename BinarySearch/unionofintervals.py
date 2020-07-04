class UnionOfIntervals:
    def nthElement(self,lowerBound,upperBound,n):
        lo = min(lowerBound)
        hi = max(upperBound)
        l = len(lowerBound)
        while(lo<=hi):
            pos = 0
            mid = lo + ((hi-lo)//2)
            for i in range(l):
                if lowerBound[i]<= mid:
                    if upperBound[i]>=mid:
                        pos += mid - lowerBound[i]+1
                    else:
                        pos += upperBound[i]-lowerBound[i]+1
            if pos > n: 
                hi = mid -1
            else:
                lo = mid+1
        return lo
